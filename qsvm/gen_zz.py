import warnings
import sys
warnings.filterwarnings('ignore')

from datetime import datetime
from time import time
from math import ceil
from qiskit import IBMQ
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import QiskitRuntimeService, Options, Session, Estimator
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

from svmtools import getSVMU

def log(st): # blue
    print("LOG: \033[94m" + st + "\033[0m")

def timer(s,e): # green
    c = int((e-s)/6)/10; # min with 1 decimal
    st = "\033[92m" + str(c+1) + "min\033[0m"
    return st

# DATA
train_data = np.load('train_data.npy')
train_labels = np.load('train_labels.npy')
test_data = np.load('test_data.npy')
test_labels = np.load('test_labels.npy')

log("Starting lower depth Program smaller ZZFeatureMap")

"""
=================
TRAIN DATA
=================
"""

# ZZ & ZZ.T
SIZE = 6
fidelity_c = getSVMU(SIZE)

def data_append(n, x1, x2):
    para_data = []
    for i in range(n):
        for j in range(i + 1, n):
            para_data.append(
                list(x1[i]) + list(x2[j])
            )

    return para_data

log("Circuits Created")

# authenticate at Qiskit runtime service
IBMQ.load_account()
service = QiskitRuntimeService()
# backend = service.backends(simulator=False)[20] # washington
backend = service.get_backend("ibmq_qasm_simulator")
options = Options(
    simulator={"seed_simulator": 42},
    resilience_level=0
)

print(f"Using: {backend} with Circuit Depth: {fidelity_c.depth()} and {fidelity_c.num_qubits} qubits")

n = len(train_data)
circuit_num = int(n * (n - 1) / 2)

parameter_values_arr=data_append(n, train_data, train_data)
circ_limit = 1200
num_jobs = ceil(circuit_num / circ_limit)

log("Starting Estimator on "+str(num_jobs)+" jobs")
shots = 2**(SIZE+3)
# this decides the basis of the observable
I = SparsePauliOp.from_list([("I",1)])
Z = SparsePauliOp.from_list([("Z",1)])
# TODO: unknown why Z+I/2 is used
O = (Z+I)/2
# use the same observable for all qubits
# we need prob of 0,0,0... for all qubits
# returns O^O^O^...^O
O_N = O
for _ in range(SIZE-1):
    O_N ^= O

start_time = time()
for i in range(num_jobs):
    with Session(service=service, backend=backend):
        estimator = Estimator(options=options)
        if i > 0:
            sys.stdout.write("\033[F") #back to previous line
        log("Running Job: "+str(i+1)+"/"+str(num_jobs))
        start_idx = circ_limit * i
        end_idx = circ_limit * (i + 1) if i < num_jobs - 1 else circuit_num
        job = estimator.run(
            circuits=[fidelity_c] * (end_idx - start_idx),
            observables=[O_N] * (end_idx - start_idx),
            parameter_values=parameter_values_arr[start_idx:end_idx],
            shots=shots
        )
        fidelity_estimator_noise1 = job.result()
        fidelity_estimator_noise = (
            fidelity_estimator_noise1.values
            if i == 0
            else np.hstack((
                fidelity_estimator_noise,
                fidelity_estimator_noise1.values
            ))
        )

print('training time:'+timer(start_time,time()))

# based on current data
# Kern em = 100x99/2 (n(n-1)/2)
kernel_em = [
    fidelity_estimator_noise[i]
    for i in range(circuit_num)
]

K = np.zeros((n,n))
tri_indices = np.triu_indices(n, k=1)
K[tri_indices] = kernel_em[0:]
K += K.T + np.eye(n)

print(K)
svc = SVC(kernel='precomputed')

log("Testing SVM...")
"""
=================
TEST DATA
=================
"""

svc.fit(K, train_labels)

n1 = len(test_data)
n2 = len(train_data)
circuit_num_1 = n1*n2 # build your code here
print(circuit_num_1)
def data_append_1(n1, n2, x1, x2):
    para_data_1 = []
    for i in range(n1):
        for j in range(n2):
            para_data_1.append(
                list(x1[i])+list(x2[j])
            )
    return para_data_1


para_vals = data_append_1(n1, n2, test_data, train_data)
num_jobs_1 = ceil(circuit_num_1/circ_limit)

np.save('kernel_washington.npy', K)
kk = np.load('kernel_washington.npy')
print(kk)

log("Starting Testimator on "+str(num_jobs_1)+" jobs")

start_time = time()
for i in range(num_jobs_1):
    with Session(service=service, backend=backend):
        estimator = Estimator(options=options)
        if i > 0:
            sys.stdout.write("\033[F") #back to previous line
        log("Running Job: "+str(i+1)+"/"+str(num_jobs_1))
        start_idx = circ_limit * i
        end_idx = (circ_limit * (i + 1)
            if i < num_jobs_1 - 1
            else circuit_num_1
        )
        job = estimator.run(
            circuits=[fidelity_c] * (end_idx - start_idx),
            observables=[O_N] * (end_idx - start_idx),
            parameter_values=parameter_values_arr[start_idx:end_idx],
            shots=shots
        )
        fidelity_estimator_noise1 = job.result()
        fidelity_estimator_noise_1 = (
            fidelity_estimator_noise1.values
            if i == 0
            else np.hstack((
                fidelity_estimator_noise_1,
                fidelity_estimator_noise1.values
            ))
        )

print('testing time:'+timer(start_time,time()))

kernel_1 = [
    fidelity_estimator_noise_1[i]
    for i in range(circuit_num_1)
]

K_1 = np.array(kernel_1).reshape(n1, n2)
print("Shape of K_1: ", K_1.shape)

predict_test = svc.predict(K_1)
report = classification_report(test_labels,predict_test, output_dict=True)
matrix = confusion_matrix(test_labels,predict_test)
print(
    "Report: ", report, "\n",
    "Matrix: ", matrix
)

with open('results.json', 'w') as f:
    f.write(str(report))

log(f"Done at {datetime.now().strftime('%H:%M:%S')}")