import warnings
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
import numpy as np
from torch import sum, save, tensor
from torch.optim import Adam
from torch.optim.lr_scheduler import ExponentialLR
from torch.utils.data import DataLoader, Subset

# local imports
from model.qutils import QDataSet
from model.index import AutoDenoiser
from tools import rtol, get, my_loss, PCTLoss

PATH_train = "./pandad/clean_sim.csv"
PATH_test = "./pandad/fuzzy.csv"


def run():
    return print("EMERGENCY STOP!")
    # train on Simulator, test on Actual
    trainset = QDataSet(PATH_train)
    testset = QDataSet(PATH_test)
    # a random 10%
    testset = Subset(testset, list(range(0, len(testset), 10)))

    train_dataloader = DataLoader(trainset, batch_size=8, shuffle=True)
    test_dataloader = DataLoader(testset, batch_size=1, shuffle=True)

    # model:
    model = AutoDenoiser()
    opt = Adam(model.parameters(), lr=5e-5)
    scheduler = ExponentialLR(opt, 0.999)
    epochs = 5000
    losses = []

    # train
    early_stop = False
    losses = [200]
    for epoch in tqdm(range(epochs)):
        if early_stop:
            break
        for idx, batch in enumerate(train_dataloader):
            opt.zero_grad()

            qubits = batch["qubits"]
            noisy = batch["noisy"]
            ideal = batch["ideal"]

            pred = model(noisy, qubits)
            loss = sum(my_loss(pred, ideal, noisy))

            loss_scalar = loss.cpu().item()

            # save loss if it is less than previous value
            if (loss_scalar < losses[-1]):
                losses.append(loss_scalar)

            loss_pct = PCTLoss(loss_scalar, scale=10)

            if (loss_pct <= 0.95):  # 0.9 loss kill
                print(f"Early Stop Loss: {loss_pct}%")
                early_stop = True
                break

            loss.backward()
            opt.step()
        scheduler.step()

    save(model.state_dict(), "./model/wnb.pth")

    model.eval()
    for idx, batch in enumerate(test_dataloader):
        if (idx % int(len(test_dataloader)/40) == 0):
            qubits = batch["qubits"]
            noisy = batch["noisy"]
            ideal = batch["ideal"]

            preds = model(noisy, qubits).detach()

            # preprocess preds
            # for each value within tol of 0.005 round to 0, 0.5 or 1
            preds = np.where(rtol(preds, 0), 0, preds)
            preds = np.where(rtol(preds, 1), 1, preds)
            # zero out first 8-qubits values
            for i in range(8-qubits):
                preds[0][i] = 0.0001

            # back to tensor
            preds = tensor(preds)
            dist = PCTLoss(sum(my_loss(preds, ideal, noisy)), scale=10)

            print(
                f"Noisy: {get(noisy)}\n",
                f"Ideal: {get(ideal)}\n",
                f"Preds: {get(preds)}\n",
                f"Test {idx} Error: {dist}%\n"
            )

    # make plot for losses and gains
    losses = losses[1:]
    print(f"LOSS CHANGE\nMax: {losses[0]} - Min: {losses[-1]}")
    plt.plot(losses)
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.show()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    run()
