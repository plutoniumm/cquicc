import torch.optim as optim
from torch.nn import (
 Module, Linear, Dropout2d, CrossEntropyLoss,
 Conv2d, MaxPool2d, Flatten, ReLU, Sequential
)
import torch.nn.functional as F
from utils import gtt


train_loader, test_loader = gtt(100, [i for i in range(10)])

print("Train loader length: ", len(train_loader))
print("Test loader length: ", len(test_loader))

class Convy(Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.conv1 = Conv2d(1, 6, kernel_size=3)
        self.dropout1 = Dropout2d(0.25)
        self.conv2 = Conv2d(6, 16, kernel_size=3)
        self.dropout2 = Dropout2d(0.25)
        self.conv3 = Conv2d(16, 32, kernel_size=3)
        self.dropout3 = Dropout2d(0.25)
        self.fc1 = Linear(32, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = self.dropout2(x)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2)
        x = self.dropout3(x)
        x = x.view(x.shape[0], -1)
        x = self.fc1(x)
        return x


model4 = Convy()
optimizer = optim.Adam(model4.parameters(), lr=0.001)
loss_func = CrossEntropyLoss()

loss_list = []  # Store loss history
model4.train()  # Set model to training mode
epochs = 100  # Set number of epochs
for epoch in range(epochs):
    total_loss = []
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad(set_to_none=True)  # Initialize gradient
        output = model4(data)  # Forward pass

        loss = loss_func(output, target).unsqueeze(-1)
        loss.backward()  # Backward pass

        optimizer.step()  # Optimize weights
        total_loss.append(loss.item())  # Store loss
    loss_list.append(sum(total_loss) / len(total_loss))
    print("Training [{:.0f}%]\tLoss: {:.4f}".format(100.0 * (epoch + 1) / epochs, loss_list[-1]))


model4.eval()  # set model to evaluation mode
correct = 0
for batch_idx, (data, target) in enumerate(test_loader):
    output = model4(data)
    if len(output.shape) == 1:
        output = output.reshape(1, *output.shape)


    pred = output.argmax(dim=1, keepdim=True).squeeze(-1)
    correct += pred.eq(target.view_as(pred)).sum().item()

    loss = loss_func(output, target)
    total_loss.append(loss.item())

print(
  "Performance on test data:\n\tLoss: {:.4f}\n\tAccuracy: {:.1f}%".format(
    sum(total_loss) / len(total_loss),
    correct * 100 / len(test_loader)
  )
)
