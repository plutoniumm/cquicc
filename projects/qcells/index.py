import torch.optim as optim
from torch.nn import CrossEntropyLoss
from utils import gtt
from torch.nn import (
 Module, Linear, Dropout2d, Conv2d
)
from torch.nn.functional import relu, max_pool2d
from quanv import Quanv

# USE_CONV = Conv2d
USE_CONV = Quanv
LOG_FREQ = 3

train_loader, test_loader = gtt(100, [i for i in range(10)])
print("Train loader length: ", len(train_loader))
print("Test loader length: ", len(test_loader))
print(f"Using Conv Style {USE_CONV.__name__}. Logging every {LOG_FREQ}%")

class Convy(Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.conv1 = USE_CONV(1, 6, kernel_size=3)
        self.dropout1 = Dropout2d(0.25)
        self.conv2 = USE_CONV(6, 16, kernel_size=3)
        self.dropout2 = Dropout2d(0.25)
        self.conv3 = USE_CONV(16, 32, kernel_size=3)
        self.dropout3 = Dropout2d(0.25)
        self.fc1 = Linear(32, 10)

    def forward(self, x):
        x = relu(self.conv1(x))
        x = max_pool2d(x, 2)
        x = self.dropout1(x)
        x = relu(self.conv2(x))
        x = max_pool2d(x, 2)
        x = self.dropout2(x)
        x = relu(self.conv3(x))
        x = max_pool2d(x, 2)
        x = self.dropout3(x)
        x = x.view(x.shape[0], -1)
        x = self.fc1(x)
        return x

model4 = Convy()
optimizer = optim.Adam(model4.parameters(), lr=0.001)
loss_func = CrossEntropyLoss()

loss_list = []  # Store loss history
model4.train()  # Set model to training mode
epochs = 150  # Set number of epochs
for epoch in range(epochs):
    total_loss = []
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad(set_to_none=True)  # Initialize gradient
        output = model4(data)  # Forward pass

        loss = loss_func(output, target).unsqueeze(-1)
        loss.backward()  # Backward pass

        optimizer.step()  # Optimize weights
        l = loss.item()
        # if nan terminate
        if l != l:
            print("Loss is nan. Terminating")
            exit()

        total_loss.append(l)  # Store loss

    loss_list.append(sum(total_loss) / len(total_loss))

    pct = int(100 * (epoch + 1) / epochs)
    if pct % LOG_FREQ == 0:
        print("Training [{:.0f}%]\tLoss: {:.4f}" .format(
            pct, sum(total_loss) / len(total_loss)
        ))


model4.eval()  # set model to evaluation mode
correct = 0
for batch_idx, (data, target) in enumerate(test_loader):
    output = model4(data)
    if len(output.shape) == 1:
        output = output.reshape(1, *output.shape)

    pred = output.argmax(dim=1, keepdim=True).squeeze(-1)
    correct += pred.eq(target.view_as(pred)).sum().item()

    # print output & pred
    print(f"Output: {output}, Pred: {pred}")

    loss = loss_func(output, target)
    total_loss.append(loss.item())

print(
  "Performance on test data:\n\tLoss: {:.4f}\n\tAccuracy: {:.1f}%".format(
    sum(total_loss) / len(total_loss),
    correct * 100 / len(test_loader)
  )
)
