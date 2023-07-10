# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# from ibm_quantum_widgets import *
from qiskit_aer import AerSimulator
import numpy as np
import pandas as pd
import csv

from ..tools import getRandCircuit, getBitwise

# qiskit-ibmq-provider has been deprecated.
# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.circuit.random import random_circuit

f = open("./path.csv", "w+")
writer = csv.writer(f)
writer.writerow(["index", "qubits", "sys_noisy",
                "sys_ideal", "ideal", "noisy"])


def writeToCsv(
    qubits,
    noisy, ideal,
    backend_noisy, backend_ideal,
    csv_file=f
):
    for i in range(len(noisy)):
        writer.writerow([
            i, qubits,
            backend_noisy, backend_ideal,
            ideal[i], noisy[i]]
        )


QiskitRuntimeService.delete_account()
QiskitRuntimeService.save_account(
    channel="ibm_quantum", token=token, overwrite=True)

# Loading your IBM Quantum account(s)
service_ideal = AerSimulator()
backend_ideal = "AerSimulator"

service_noisy = QiskitRuntimeService()
backend_noisy = "ibmq_kolkata"
service_noisy.backend = backend_noisy

sampler_noisy = Sampler(session=backend_noisy)
sampler_ideal = service_ideal


def runCircuits(num_qubits, num_circuits):
    generated = [getRandCircuit(num_qubits) for _ in range(num_circuits)]
    job_noise = sampler_noisy.run(generated)
    job_ideal = sampler_ideal.run(generated)

    id_nz = job_noise.job_id()
    id_id = job_ideal.job_id()

    print(f"NOISE ID: {id_nz} | IDEAL ID: {id_id}")

    result_nz = job_noise.result()
    result_id = job_ideal.result()

    result_nz = [getBitwise(i, 10) for i in result_nz.quasi_dists]
    result_id = [getBitwise(i, 2) for i in result_id.get_counts()]

    return result_nz, result_id


batch = 300

for qubits in [i for i in range(4, 9, 2)] * 2:
    noisy, ideal = runCircuits(qubits, batch)
    writeToCsv(qubits, noisy, ideal, backend_noisy, backend_ideal)
    print(f"Circuits Ran {qubits}!!")
f.close()

print(f"EXPECTED LEN {batch * 5}")
