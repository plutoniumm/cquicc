from qiskit import QuantumCircuit
def testCirc():
    qc = QuantumCircuit(5)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.cx(0, 4)
    qc.x(3)
    qc.rx(10, 0)
    qc.cx(2, 4)
    qc.ry(55, 3)
    qc.measure_all()

    return qc