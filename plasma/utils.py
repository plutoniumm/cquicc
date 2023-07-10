from numpy import array, append, where, sum, sqrt
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
from qiskit.utils import algorithm_globals


"""
NUMBER DIGITS
"""
# Define the indices for the digits
def zero_idx(i, j):  # Index for zero pixels
    return [
        [i-1, j], [i-1, j - 1], [i-1, j - 2], [i-1, j - 3],
        [i, j+1], [i, j - 4],
        [i+1, j], [i+1, j - 1], [i+1, j - 2], [i+1, j - 3],
    ]


def one_idx(i, j):
    return [[i, j - 1], [i, j - 2], [i, j - 3], [i, j - 4], [i, j - 5], [i - 1, j - 4], [i, j]]


def two_idx(i, j):
    return [[i-1, j - 1], [i, j - 2], [i+1, j - 3], [i+1, j - 4], [i, j - 5], [i - 1, j - 4],
            [i, j], [i-1, j], [i+1, j]]


def get_dataset_digits(num, draw=True):
    # Create Dataset containing zero and one
    train_images = []
    train_labels = []

    func = [zero_idx, one_idx, two_idx]
    internal_dim = 64
    for number in range(3):
        for i in range(int(num / 2)):
            # First we introduce background noise
            empty = array(
                [algorithm_globals.random.uniform(
                    0, 0.05) for i in range(internal_dim)]
            ).reshape(8, 8)

            # Now we insert the pixels for the one
            for i, j in func[number](2, 6):
                empty[j][i] = algorithm_globals.random.uniform(0.86, 1)
            train_images.append(empty)
            train_labels.append(number)
            if draw:
                plt.rcParams["figure.figsize"] = (2, 1)
                plt.title(f"This is a {number}")
                plt.imshow(train_images[-1])
                plt.show()

    train_images = array(train_images)
    train_images = train_images.reshape(len(train_images), internal_dim)

    for i in range(len(train_images)):
        sum_sq = sum(train_images[i] ** 2)
        train_images[i] = train_images[i] / sqrt(sum_sq)

    return train_images, train_labels


"""
CIFAR DATASET
"""


def get_dataset_cifar(num, trainset, draw=True):
    # Create Dataset containing zero and one
    train_images = []
    train_labels = []

    for tup in trainset:
        train_images.append(tup[0])
        train_labels.append(tup[1])

    train_images = array(train_images)
    train_labels = array(train_labels)

    return train_images, train_labels


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
