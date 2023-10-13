## Speakernotes for CKT1

1. **Home slide**: What is circuit cutting
- Cutting a circuit into smaller circuits by modifying gates or wires

2. **Why Circuit cutting**: Why do we want to cut circuits &rarr; NOISE
3. **What is noise**:
- When we do H we should se 50-50 but we dont
- What are sources of noise
- What is noise simulation
- Lets simulate a predefined circuit for N blocks
- Show noise increases with N even if result is known/does not change
- Conclude smaller circuits are better for less noise therefore we need to cut circuits

4. **Gate Cuts**: How to cut gates
- Split horizontally
- We sample and replace CNOT with some known gates (we will see how to calculate this later)
- We now have 2-2, we can also do 1-3 or 3-1
5. **Wire Cuts**: How to cut wires
- Split vertically
- We convert wire cuts into move instructions
- We then apply gate cuts to move gate
- Maybe talk about how q-2 is thrown out depending upon audience response...?

6. **Sample Breakdown**: Explain superficially gate decomposition with CNOT
7. **Example problem with code**: 4-GHZ -> 2-2
- Show steps
- Make circuit & create observables
- Define cuts & see cut circuits
- Calculate subcircuits & reconstruction weights
- Run & Stats

8. **Open Questions**:
- I am working on automating the 'Define Cuts' step
- How does this work at scale is unknown
- How to cut down overhead:
  - Example: From CutQC -> Qiskit they started random sampling rather than full calculation of all states since most of it is 0
- How can we cut better without going from 1 NP-hard &rarr; another NP-hard problem
- Resources