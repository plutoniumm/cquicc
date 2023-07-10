import warnings
import numpy as np
from torch import sum, load, tensor
from torch.utils.data import DataLoader, Subset

# local imports
from model.qutils import QDataSet
from model.index import AutoDenoiser
from tools import rtol, get, my_loss, PCTLoss

PATH_test = "./pandad/cleaned.csv"


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testset = QDataSet(PATH_test)
    # a random 10%
    testset = Subset(testset, list(range(0, len(testset), 10)))
    test_dataloader = DataLoader(testset, batch_size=1, shuffle=True)

    # model:
    model = AutoDenoiser()

    model.load_state_dict(load("./model/wnb.pth"))
    model.eval()
    losses = []
    for idx, batch in enumerate(test_dataloader):
        if (idx % int(len(test_dataloader)/10) == 0):
            qubits = batch["qubits"]
            noisy = batch["noisy"]
            ideal = batch["ideal"]

            preds = model(noisy, qubits).detach()

            # preprocess preds
            # for each value within tol of 0.005 round to 0, or 1
            preds = np.where(rtol(preds, 0), 0, preds)
            preds = np.where(rtol(preds, 1), 1, preds)
            # zero out first 8-qubits values
            for i in range(8-qubits):
                preds[0][i] = 0.0001

            # back to tensor
            preds = tensor(preds)

            dist = PCTLoss(sum(my_loss(preds, ideal, noisy)), scale=10)

            # if error is greater than 15%, skip printing
            print(
                f"Noisy: {get(noisy)}\n",
                f"Ideal: {get(ideal)}\n",
                f"Preds: {get(preds)}\n",
                f"Test {idx} Error: {dist}%\n"
            )
            losses.append(dist)

    print(f"Average Error: {np.average(losses)}%")