import numpy as np

def matrix_transpose(arr):
    new_arr = [[] for _ in range(len(arr[0]))]

    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            new_arr[j].append(row[j])

    return new_arr

def parse_circuit(string):
    if string.endswith(".qc"):
        with open(string, "r") as file:
            string = file.read()

    lines = string.split("\n")
    lines = [e.strip() for e in lines if not e.startswith("//")]

    by_rows = [list(filter(None, e.split(" "))) for e in lines]

    # Transpose the matrix
    return matrix_transpose(by_rows)


def get_param(s: str) -> str:
    if "(" not in s or ")" not in s:
        return None

    param = s[s.index("(") + 1:s.index(")")]
    return param

def get_gate(s: str) -> str:
    if "(" in s and ")" in s:
        s = s[:s.index("(")]

    return s

def apply_gate(s: str, index: int) -> str:
    gate = get_gate(s)
    param = get_param(s)

    if param:
        return Q[gate](index, param)
    return Q[gate](index)

def resolve_layer(layer: list) -> str:
    layer_gates = [apply_gate(e, i) for i, e in enumerate(layer) if apply_gate(e, i) is not None]
    indented_gates = ["    " + gate for gate in layer_gates]

    return "\n".join(indented_gates)

def resolve_circuit(circuit, name):
    circuit_gates = "\n".join(map(resolve_layer, circuit))
    circuit_gates = f'from qiskit import QuantumCircuit\ndef {name}():\n    qc = QuantumCircuit({len(circuit[0])})\n    {circuit_gates}\n    qc.measure_all()\n    return qc'

    return circuit_gates

# Define your parseCircuit function and other necessary functions here

# TEST START
name = "circuit"
circuit = parse_circuit(f'./{name}.qc')
resolved = resolve_circuit(circuit, "testCirc")
with open(f'./{name}.py', 'w') as f:
    f.write(resolved)
# TEST END


import os

def file2str(name):
    with open(name, "r") as file:
        str_content = file.read()
    return parse_circuit(str_content)

def file2file(name):
    circuit = file2str(name)
    resolved = resolve_circuit(circuit, "testCirc")
    with open(f"{name}.py", "w") as file:
        file.write(resolved)
    return True

def str2str(str_content):
    circuit = parse_circuit(str_content)
    return resolve_circuit(circuit, "testCirc")

def str2file(str_content, name):
    resolved = str2str(str_content)
    with open(f"{name}.py", "w") as file:
        file.write(resolved)
    return True

def main():
    has_gates = ", ".join(Q.keys())  # Assuming Q is a predefined dictionary.
    print(f"hasGates: {has_gates}")

if __name__ == "__main__":
    main()
