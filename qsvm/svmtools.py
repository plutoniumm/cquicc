from random import choice
from string import ascii_lowercase
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import ZZFeatureMap

def rnd(prefix):
    st = ''.join(choice(ascii_lowercase) for _ in range(3))

    return st if prefix is None else prefix + st

# # FOR 2 coupling
# def getZZ(sz, prefix=None):
#     if prefix is None:
#         prefix = rnd(None)
#     f0 = QuantumCircuit(sz)
#     for i in range(0, sz, 2):
#         f0.append(ZZFeatureMap(2, reps=1, parameter_prefix=rnd(prefix), entanglement='full'), [i,i+1])

#     for i in range(1, sz-1, 2):
#         f0.cx(i, i+1)

#     f0.cx(sz-1, 0)
#     return f0.decompose()

# FOR 3 coupling
def getZZ(sz, prefix=None):
    if prefix is None:
        prefix = rnd(None)
    f0 = QuantumCircuit(sz)
    for i in range(0, sz, 3):
        f0.append(
            ZZFeatureMap(3, reps=1, parameter_prefix=rnd(prefix), entanglement='full'),
            [i,i+1,i+2]
        )

    for i in range(2, sz-2, 3):
        f0.cx(i, i+1)

    return f0.decompose()

def getSVMU(sz):
  # make ZZ & ZZ.T
  fid = getZZ(sz, prefix="x")
  fid.append(
      getZZ(sz, prefix="y").inverse(),
      range(fid.num_qubits)
  )
  fid.measure_all()

  # transpile
  fid2 = transpile(
    fid.decompose().decompose(),
    optimization_level=3
  )

  return fid2