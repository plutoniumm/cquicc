from qiskit.providers.fake_provider import FakeManilaV2
from qiskit.providers.aer.noise import NoiseModel
from qiskit import QuantumCircuit, transpile
from qiskit import Aer, execute
from json import dump
from abrax import A

qc = QuantumCircuit(4)
backend = FakeManilaV2()
model = NoiseModel.from_backend(backend)
simulator = Aer.get_backend('qasm_simulator')
gates = model.basis_gates
cmap = simulator.configuration().coupling_map

def addLayer(qc):
  # it appends automatically :)
  qc = A(f"""
  - -     H
  - CX(0) H
  - CX(1) H
  - CX(2) H
""", qc, {'measure': False})
  return qc

def run(qc):
  qc2 = qc.copy()
  qc2.measure_all()
  t_circuit = transpile(qc2, backend)

  result = execute(t_circuit, simulator,
    shots=2**13,
    noise_model=model,
    coupling_map=cmap,
    basis_gates=gates
  ).result().get_counts(t_circuit)

  return result

count_list = []
for i in range(15):
  for _ in range(8):
    qc = addLayer(qc)

  counts = run(qc)
  count_list.append(counts)
  print(f"Done {i+1}/15")

with open('count_list.json', 'w') as f:
  dump(count_list, f)