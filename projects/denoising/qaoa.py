import numpy as np
from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp
from qiskit.visualization import plot_distribution
from qiskit_ibm_runtime import (
  QiskitRuntimeService, Estimator, Sampler, Session
)
from scipy.optimize import minimize
from encoder.tools import getBitwise

print("Running QAOA")

service = QiskitRuntimeService()
backend = service.get_backend("ibmq_qasm_simulator")

hamiltonian = SparsePauliOp.from_list(
    [("IIIZZ", 1), ("IIZIZ", 1), ("IZIIZ", 1), ("ZIIIZ", 1)]
)

ansatz = QAOAAnsatz(hamiltonian, reps=2)
ansatz.decompose().draw("mpl")

# ndarray, QuantumCircuit, SparsePauliOp, Estimator primitive
def cost_func(params, ansatz, hamiltonian, estimator):
    # Returns: float: Energy estimate
    return  (
        estimator.run(ansatz, hamiltonian, parameter_values=params).result().values[0]
    )

session = Session(backend=backend)
estimator = Estimator(session=session, options={"shots": 1024})
sampler = Sampler(session=session, options={"shots": 1024})

x0 = 2 * np.pi * np.random.rand(ansatz.num_parameters)

print(f"Initial parameters: {x0}")

res = minimize(cost_func, x0, args=(ansatz, hamiltonian, estimator), method="COBYLA")

# Assign solution parameters to ansatz
qc = ansatz.assign_parameters(res.x)
# Add measurements to our circuit
qc.measure_all()

print("Running sampler")

# Sample ansatz at optimal parameters
samp_dist = sampler.run(qc, shots=int(1024)).result().quasi_dists[0]
bitwise = getBitwise(samp_dist, 10)

print(bitwise)

print("Bringing in the Guns")

import warnings
from torch import sum, load, tensor
from torch.utils.data import DataLoader, Subset
from encoder.model.qutils import QDataSet
from encoder.model.index import AutoDenoiser
from encoder.tools import rtol, get, my_loss, PCTLoss

PATH_test = "./encoder/pandad/cleaned.csv"

testset = QDataSet(PATH_test)
# a random 10%
testset = Subset(testset, list(range(0, len(testset), 10)))
test_dataloader = DataLoader(testset, batch_size=1, shuffle=True)

model = AutoDenoiser()
model.load_state_dict(load("./encoder/model/wnb.pth"))

print("Running Model")
model.eval()

qubits = 8
bitwise = np.ndarray([bitwise])
print(f"Denoising {bitwise} with {qubits} qubits");

preds = model(bitwise, qubits).detach()

# preprocess preds
# for each value within tol of 0.005 round to 0, or 1
preds = np.where(rtol(preds, 0), 0, preds)
preds = np.where(rtol(preds, 1), 1, preds)
# zero out first 8-qubits values
for i in range(8-qubits):
    preds[0][i] = 0.0001

# back to tensor
preds = tensor(preds)
print(preds)