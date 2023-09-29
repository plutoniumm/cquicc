import { writeFileSync, readFileSync } from "fs";
import Q from "./gates";

const matrixTranspose = (arr: string[][]) => {
  const newArr = new Array(arr[0].length)
    .fill(0).map(e => []);

  for (let i = 0; i < arr.length; i++) {
    const row = arr[i];
    for (let j = 0; j < row.length; j++) {
      newArr[j].push(row[j]);
    }
  }

  return newArr;
}

function parseCircuit (string: string): string[][] {
  if (string.endsWith(".qc")) {
    string = readFileSync(string, "utf8");
  }

  const lines = string
    .split("\n")
    .map(e => e.trim())
    .filter(e => e.slice(0, 2) !== "//")

  /*[
    - H CX5 RX(10)
    - H -    -
    - H -    -
    - H X    -
    - H -    -
  ]*/

  const byRows = lines.map(l => l
    .split(" ")
    .map(e => e.trim())
    .filter(e => e !== "")
  );

  // byCols
  return matrixTranspose(byRows);
};

/*
 - - - - -
 H H H H H
 CX5 - - X -
 RX(10) - - - -
 - - - - - -
*/
function getParam (str: string): string | null {
  if (
    !str.includes("(") ||
    !str.includes(")")
  ) return null;

  const param = str.slice(
    str.indexOf("(") + 1,
    str.indexOf(")")
  );
  return param;
}

function getGate (str: string): string {
  if (
    str.includes("(") && str.includes(")")
  ) str = str.slice(0, str.indexOf("("));

  return str;
}

function applyGate (str: string, index: number): string | null {
  let [gate, param] = [getGate(str), getParam(str)];

  if (param)
    return Q[gate](index, param);
  return Q[gate](index);
}

function resolveLayer (layer: string[]): string {
  const layerGates = layer
    .map((e, i) => applyGate(e, i))
    .filter(Boolean)
    .map(e => "    " + e)

  return layerGates.join("\n");
}

function resolveCircuit (circuit: string[][], name: string): string {
  let circuitGates = circuit
    .map(resolveLayer)
    .join("\n");

  circuitGates = `from qiskit import QuantumCircuit
def ${name}():
    qc = QuantumCircuit(${circuit[0].length})
    ${circuitGates.trim()}
    qc.measure_all()

    return qc`

  return circuitGates;
}

// TEST START
const name = "circuit"
const circuit = parseCircuit(`./${name}.qc`);
const resolved = resolveCircuit(circuit, "testCirc");
writeFileSync(`./${name}.py`, resolved);
// TEST END

function file2str (name: string): string[][] {
  const str = readFileSync(name, "utf8");
  return parseCircuit(str);
}

function file2file (name: string): boolean {
  const circuit = file2str(name);
  const resolved = resolveCircuit(circuit, "testCirc");
  writeFileSync(`./${name}.py`, resolved);
  return true;
}

function str2str (str: string): string {
  const circuit = parseCircuit(str);
  return resolveCircuit(circuit, "testCirc");
}

function str2file (str: string, name: string): boolean {
  const resolved = str2str(str);
  writeFileSync(`./${name}.py`, resolved);
  return true;
}

export default {
  hasGates: Object.keys(Q).join(", "),
  file2str,
  file2file,
  str2str,
  str2file,
}