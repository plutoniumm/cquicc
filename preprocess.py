import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from lib.utils import warn

import sys

# see if file is provided
if len(sys.argv) < 2:
  warn("Usage: python preprocess.py <filename.csv>")
  file=input("Enter filename: ")
  if(len(file) == 0):
    warn("No filename provided. Exiting...")
    file="e1200.csv"
else:
  file=sys.argv[1]

# Assuming your data is loaded into a variable called 'data'
data = np.genfromtxt(file, delimiter=',', skip_header=1)
X = data[:, 1:-1]  # Features excluding index and Engine Condition
y = data[:, -1]    # Engine Condition (labels)

"""
DO NOT UNDER ANY CIRCUMSTANCES USE THIS FOR OTHER DATASETS.
THIS IS A VERY SPECIFIC PREPROCESSING PIPELINE FOR THE ENGINE DATASET SINCE WE KNOW THE DISTRIBUTION OF THE DATA.
"""
# Remove both X,y if X outside [-3,3] and then normalise to [-1,1] for each feature
for i in range(X.shape[1]):
  y = y[np.logical_and(X[:, i] > -2, X[:, i] < 2)]
  X = X[np.logical_and(X[:, i] > -2, X[:, i] < 2)]
  X[:, i] = (X[:, i] - X[:, i].min()) / (X[:, i].max() - X[:, i].min()) * 2 - 1

# if your random_seed != 42, are you even a data scientist?
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
)

# convert to fp16
X_train = X_train.astype(np.float16)
X_test = X_test.astype(np.float16)
y_train = y_train.astype(np.float16)
y_test = y_test.astype(np.float16)

np.save('train_data.npy', X_train)
np.save('train_labels.npy', y_train)
np.save('test_data.npy', X_test)
np.save('test_labels.npy', y_test)

## Visualising the distribution of train data
for i in range(X.shape[1]):
  plt.hist(X[:, i], bins=50, alpha=0.8)
plt.savefig('train_distri.png')