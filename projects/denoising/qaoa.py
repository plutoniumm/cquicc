import numpy as np
from qiskit.circuit.library import QAOAAnsatz
from qiskit.quantum_info import SparsePauliOp
from qiskit.visualization import plot_distribution
from qiskit_ibm_runtime import (
  QiskitRuntimeService, Estimator, Sampler, Session
)
from scipy.optimize import minimize
from encoder.tools import getBitwise


print("Running Program")

service = QiskitRuntimeService()
backend = service.get_backend("ibmq_qasm_simulator")

hamiltonian = SparsePauliOp.from_list(
    [("IIIZZ", 1), ("IIZIZ", 1), ("IZIIZ", 1), ("ZIIIZ", 1)]
)

# QAOA ansatz circuit
ansatz = QAOAAnsatz(hamiltonian, reps=2)
ansatz.decompose().draw("mpl")

def cost_func(params, ansatz, hamiltonian, estimator):
    """Return estimate of energy from estimator

    Parameters:
        params (ndarray): Array of ansatz parameters
        ansatz (QuantumCircuit): Parameterized ansatz circuit
        hamiltonian (SparsePauliOp): Operator representation of Hamiltonian
        estimator (Estimator): Estimator primitive instance

    Returns:
        float: Energy estimate
    """
    cost = (
        estimator.run(ansatz, hamiltonian, parameter_values=params).result().values[0]
    )
    return cost

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
print(samp_dist)

bitwise = getBitwise(samp_dist, 10)

print(bitwise)