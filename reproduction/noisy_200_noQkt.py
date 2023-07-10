# Importing standard Qiskit libraries
from qiskit.tools.jupyter import *
from qiskit.visualization import circuit_drawer
from qiskit.circuit import ParameterVector

from sklearn import metrics
from sklearn.model_selection import train_test_split
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.algorithms import QSVC
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session, Options
from sklearn.metrics import classification_report, confusion_matrix

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile
import pandas as pd

from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit.algorithms.state_fidelities import ComputeUncompute

class QKTCallback:
  """Callback wrapper class."""
  def __init__(self) -> None:
    self._data = [[] for i in range(5)]

  def callback(self, x0, x1=None, x2=None, x3=None, x4=None):
    """
    Args:
        x0: number of function evaluations
        x1: the parameters
        x2: the function value
        x3: the stepsize
        x4: whether the step was accepted
    """
    self._data[0].append(x0)
    self._data[1].append(x1)
    self._data[2].append(x2)
    self._data[3].append(x3)
    self._data[4].append(x4)

  def get_callback_data(self):
    return self._data

  def clear_callback_data(self):
    self._data = [[] for i in range(5)]

df = pd.read_csv(r'200 EXAMPLES.csv')
ytrain,Xtrain = df.iloc[:,7], df.iloc[:,1:7]
Xtrain,Xtest , ytrain, ytest = train_test_split(Xtrain, ytrain,stratify=ytrain, test_size=0.25)
print(Xtrain,"\n",ytrain)

training_params = ParameterVector("θ", 1)

# Define the quantum circuit with PauliFeatureMap
fm0 = QuantumCircuit(6)
for i in range(6):
  fm0.rx(training_params[0], i)

# Create the feature map, composed of the two circuits
fm=ZZFeatureMap(6, entanglement='linear')
print(circuit_drawer(fm, output='mpl'))
print(f"Trainable parameters: {training_params}")
fm.draw(output="mpl")

qc=ZZFeatureMap(6, entanglement='circular')
print(transpile(qc,optimization_level=3).depth())

service = QiskitRuntimeService(channel="ibm_quantum")
print(service.backends())

backend = service.backend("ibmq_qasm_simulator")

noisy_backend = service.get_backend('ibmq_jakarta')
backend_noise_model = NoiseModel.from_backend(noisy_backend)

simulator = service.get_backend('ibmq_qasm_simulator')

options = Options()
options.resilience_level = 0
options.optimization_level = 0
options.simulator = {"noise_model": backend_noise_model}
with Session(service=service, backend=simulator) as session:
  sampler = Sampler(session=session, options=options)
  fidelity = ComputeUncompute(sampler=sampler)
  quantum_kernel = FidelityQuantumKernel(fidelity=fidelity, feature_map=fm)
  qsvc = QSVC(quantum_kernel=quantum_kernel)
  qsvc.fit(Xtrain, ytrain)

  labels_test = qsvc.predict(Xtest)

accuracy_test = metrics.balanced_accuracy_score(y_true=ytest, y_pred=labels_test)
print(f"accuracy test: {accuracy_test}")
print(confusion_matrix(ytest,labels_test))
print(classification_report(ytest,labels_test))