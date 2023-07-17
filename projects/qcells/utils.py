from numpy import array, append, where
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

"""
MNIST DATASET
"""
def gtt(n_train, filt, batch_size=64):
    n_test = int(n_train / 10)
    X_train = datasets.MNIST(root='./data', train=True, download=True,
                             transform=transforms.Compose([transforms.ToTensor()]))

    idx = array([], dtype=int)
    for label in filt:
        idx = append(idx, where(X_train.targets == label)[0][:n_train])
    X_train.data = X_train.data[idx]
    X_train.targets = X_train.targets[idx]

    train_loader = DataLoader(X_train, batch_size=batch_size, shuffle=True)

    X_test = datasets.MNIST(root='./data', train=False, download=True,
                            transform=transforms.Compose([transforms.ToTensor()]))
    idx = array([], dtype=int)
    for label in filt:
        idx = append(idx, where(X_test.targets == label)[0][:n_test])

    X_test.data = X_test.data[idx]
    X_test.targets = X_test.targets[idx]

    test_loader = DataLoader(X_test, batch_size=1, shuffle=True)

    return train_loader, test_loader


def make_filt(arr):
    filt = None
    if (arr == None):
        filt = [i for i in range(0, 10)]
    else:
        filt = arr

    digits = len(filt)

    return filt, digits
