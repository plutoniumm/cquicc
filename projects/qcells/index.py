# Additional torch-related imports
import torch
from torch import cat, no_grad, manual_seed
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.optim as optim
from torch.nn import (
 Module, Conv2d, Linear, Dropout2d, ReLU,
 NLLLoss, MaxPool2d, Flatten, Sequential,
)
import torch.nn.functional as F
from utils import gtt


train_loader, test_loader = gtt(100, [i for i in range(2)])

print("Train loader length: ", len(train_loader))
print("Test loader length: ", len(test_loader))