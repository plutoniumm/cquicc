import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
from time import time
from dimod import BinaryQuadraticModel
from neal import SimulatedAnnealingSampler
import sys
from lib.utils import timer, log

SIGMA = float(sys.argv[1]) if len(sys.argv) > 1 else 150
ITERS = 1000
PRECISION = [1, 2, 4, 8]
print_qubo = False
do_classical = False

train_data = np.load('train_data.npy')
train_labels = np.load('train_labels.npy')
test_data = np.load('test_data.npy')
test_labels = np.load('test_labels.npy')
log("Starting classical SVM with sigma="+str(SIGMA))

if do_classical:
  clf = svm.SVC(kernel='rbf', C=20)
  start_time = time()
  clf.fit(train_data, train_labels)
  print('training time for classical SVM:'+timer(start_time,time())+" for n="+str(len(train_labels)))
  y_pred = clf.predict(test_data)

  log("Results for classical SVM:")
  print(
    "Confusion Matrix:",
    confusion_matrix(test_labels, y_pred), "\n"
  )
  print(
    "Classification Report:",
    classification_report(test_labels, y_pred)
  )

train_labels = np.where(train_labels == 0, -1, train_labels)
test_labels = np.where(test_labels == 0, -1, test_labels)

# define RBF kernel
def Kernel(mat1, mat2, sigma):
  norm=np.linalg.norm(mat1-mat2)
  k = -(0.5*norm**2)/(sigma**2)
  return np.exp(k)

def map_kernel():
  n = len(train_labels)
  a = np.empty((n,n))
  for i in range(n):
    for j in range(n):
      a[i][j]=Kernel(
        train_data[i], train_data[j], SIGMA
      )
  return (a)

kern = map_kernel()
kern = kern.astype(np.float16)
print(f"Kernel matrix: {kern.shape}, calculated by doing Kernel(x_i, x_j, sigma) for all NC2 pairs of x_i, x_j")

def QUBO(precision):
  n = len(train_labels)
  pp = np.kron(
    np.identity(n),
    np.array(precision)
  )
  print(f"pp: {pp.shape}, calculated by doing np.kron(np.identity(n), np.array(PRECISION)). This creates a diagonal matrix of 1s and 2s [\n[...PRECISION, 0..]\n[0,...PRECISION,0..]\n...\n[0,...,...PRECISION]\n]")
  xy = np.multiply(
    kern, np.outer(train_labels, train_labels)
  )
  print("First a matrix of all values is made into an outer product s.t all rows with 1 are the training label and with 0s are zeroed out. Then this is multiplied by the kernel matrix.")
  print(f"xy: {xy.shape}, calculated by doing np.multiply(kern, np.outer(train_labels, train_labels))")

  q = np.dot(pp.T, np.dot(xy, pp)) * 0.5
  q = q - np.diag(np.dot(pp.T, np.ones(n)))
  print(f"q: {q.shape}, calculated by doing a lot of stuff tbh")
  return q, pp

qubo, pp = QUBO(PRECISION)

def bqm_to_quadratic_string(bqm):
  terms = [
    f"{value:.1f} x{str(i)} x{str(j)}"
    if i != j else f"{value:.1f}x{str(i)}"
    for (i, j), value in bqm.quadratic.items()
  ] + [
    f"{value:.1f}x{str(i)}"
    for i, value in bqm.linear.items()
  ]

  return " ".join([ term
    if term[0] == "- " else "+ " + term
    for term in terms
  ])

if print_qubo:
  eqn_string = bqm_to_quadratic_string(
    BinaryQuadraticModel.from_qubo(qubo)
  )
  print(eqn_string)

log("Generated QUBO equation")
print("QUBO:\n", qubo)

def bias_func():
  num = len(train_labels)
  a = np.zeros(num)
  for n in range(num):
      a = np.dot(sup_vec * train_labels * kern[:, n], np.ones(num))
  return np.dot(sup_vec, train_labels - a) / np.sum(sup_vec)

start_time = time()
model = BinaryQuadraticModel.from_qubo(qubo)
simAnnSamples = SimulatedAnnealingSampler().sample(
  model, num_reads=ITERS
)
mit = min(simAnnSamples.data_vectors['energy'])
print("Minimum energy:", mit)
log("Finished QUBO")

# save the values of lagrange multipliers that give minimum energy
for sample, energy, num_occ in simAnnSamples.data(['sample','energy','num_occurrences']):
  if (energy==mit):
    lagrange = np.array(list(sample.values()))
    break
lagrange = np.array(list(sample.values()))
sup_vec = np.matmul(pp,lagrange.T)
bias = bias_func()
print("Bias:", bias)
print("training time for DWave'd SVM:"+timer(start_time,time()))
log("Testing DWave'd SVM")

start_time = time()
predwave = list()
for i in range(len(test_labels)):
  n = len(train_labels)
  a = 0.0
  for k in range(n):
    a = a + \
    sup_vec[k] * train_labels[k] * Kernel(
      test_data[i], train_data[k], SIGMA
    )
  a = a + bias
  predwave.append(-1 if a<0 else 1)

print("testing time for DWave'd SVM:"+timer(start_time,time()))
print(
  "Classification Report:",
  classification_report(test_labels, predwave), "\n"
)
print(
  "Confusion Matrix:",
  confusion_matrix(test_labels, predwave)
)



"""
1200 rows
Classification Report:               precision    recall  f1-score   support

        -1.0       0.55      0.98      0.70       126
         1.0       0.80      0.11      0.19       114

    accuracy                           0.56       240
   macro avg       0.67      0.54      0.44       240
weighted avg       0.67      0.56      0.46       240


Confusion Matrix: [[123   3]
 [102  12]]
"""

"""
200 rows
Loading data...
Running SVM...
Predicting...
Accuracy: 0.425
Precision: 0.425
Recall: 0.425
F1-score: 0.425
              precision    recall  f1-score   support

         0.0       0.60      0.35      0.44        26
         1.0       0.32      0.57      0.41        14

    accuracy                           0.42        40
   macro avg       0.46      0.46      0.42        40
weighted avg       0.50      0.42      0.43        40

[[ 9 17]
 [ 6  8]]
"""