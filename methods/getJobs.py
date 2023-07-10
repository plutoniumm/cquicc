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
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit.circuit.random import random_circuit

if __name__ == "__main__":
  QiskitRuntimeService.delete_account()
  # QiskitRuntimeService.save_account(channel="ibm_cloud", token=token, instance="ibm-q-iitmadras/25x25-4/ecc25x25", overwrite=True)
  QiskitRuntimeService.save_account(channel="ibm_quantum", token=token, overwrite=True)

  # Loading your IBM Quantum account(s)
  service_ideal = AerSimulator()
  backend_ideal = "AerSimulator"

  service_noisy = QiskitRuntimeService()
  backend_noisy = "ibmq_kolkata"
  service_noisy.backend = backend_noisy

  sampler_noisy = Sampler(session=backend_noisy);
  sampler_ideal = service_ideal;

  memory = [
    # ARRAY OF JOB IDS HERE
  ]

  f = open("./path_mem.csv", "w+")
  writer = csv.writer(f)
  writer.writerow(["index", "qubits","sys_noisy", "sys_ideal", "ideal", "noisy"])

  def writeToCsv2(
    mem, backend_noisy, backend_ideal, csv_file = f
  ):
    for i in range(len(mem)):
      qubits, noisy, ideal  = mem[i]
      writer.writerow([
        i, qubits,
        backend_noisy, backend_ideal,
        ideal, noisy
      ]);

  def rc(circuit):
    result = sampler_ideal.run(circuit, memory=True)
    result = result.result().get_counts()

    return getBitwise(result, 2);

  def getFromMemory(r):
    noisy_res = [getBitwise(i,10) for i in r.result().quasi_dists]

    l = len(noisy_res);
    store = [[] for i in range(l)]
    for i in range(l):
      circ = r._params["circuits"][i]
      store[i] = [len(circ.qubits), noisy_res[i], rc(circ)]

    return store

    for cid in memory:
      print(cid)
      try:
          r = QiskitRuntimeService().job(job_id=cid)
          r = getFromMemory(r)
          writeToCsv2(r, backend_noisy, backend_ideal)
      except Exception as e:
          print(f"Error at {cid}\n{e}")
          continue
    f.close()