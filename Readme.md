# Quantum Earplugs.
Pronounced as: 'Quantum Earplugs' where the 'Bitwise Probability
Denoising AutoEncoder' is silent because you cannot hear anything with
earplugs on.

Why? Because why not?

## Usages
```py
# circuits.py
from tools import getRandCircuit, getBitwise
from noise import fakeBackendPair

qubits = 8

circuit = getRandCircuit(qubits)
noisy, ideal = fakeBackendPair(qubits)

noisy_result = noisy.run(
    circuit, shots=100, memory=True).result().get_memory()
ideal_result = ideal.run(
    circuit, shots=100, memory=True).result().get_memory()

print("Noisy bits:", getBitwise(noisy_result))
print("Ideal bits:", getBitwise(ideal_result))
# probabilities of each qubit being 1
```

## Making a Densoising Autoencoder
1. Make dataset
    A. Actual runs on Circuits to get with & without noise
2. Make Autoencoder
    a. Test against both types
    b. Add blank qubit tests for smaller circuits

## Abandoned Paths
using A random Unitary generator then adding noise to that. Because this noise will be random.
If we are to use [Qiskit Noise Model](https://qiskit.org/documentation/tutorials/simulators/3_building_noise_models.html)
we have to use generate a circuit and apply noise gate by gate and then resolve it into `ideal_result` and `noise_result`.

Then save that data to create autoencoder

## TODO
- SHould have put 1s as input instead of 0s
- Check with Choke of 2
- Check with deeper encoder [deeper decoder is a waste]
- If this is max extractable data, see how much noise was mitigated
- Benchmark for
- * AutoEncoder
- * IBMQ_Kolkata
- * IBMQ_Kolkata + AutoEncoder
- Benchmark IBMSimulator Noise vs Actual Hardware



<!-- FIXES -->
- Explain the table better (noise, pred, actual) (error should be a seperate column)
- Show data distribution (why is it lepto-kurtic)