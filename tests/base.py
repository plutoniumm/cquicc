from qiskit import QuantumCircuit
from abrax import A

qc = QuantumCircuit(4)

def addLayer(qc):
  # it appends automatically :)
  qc = A(f"""
  - -     H
  - CX(0) H
  - CX(1) H
  - CX(2) H
""", qc, {'measure': False})
  return qc

qc = A(f"""
- H
- H
- H
- H
""", qc, {'measure': False})

count_list = []
for i in range(2):
  qc= addLayer(qc)
  print(qc)