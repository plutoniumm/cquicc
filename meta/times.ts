import names from "./names.json" assert {type: 'json'};
import fs from "fs";

const GET = (url: string, opts = {}): Promise<any> =>
  fetch(url, opts).then(res => res.json());

const { sqrt, pow } = Math;

declare const Bun: any;
// mean, median, stdv
const stats = (arr: number[], mean_only = false) => {
  const len = arr.length;

  let mean = arr.reduce((a, b) => a + b, 0) / len;
  let median = arr.sort()[len / 2 | 0];
  let stdv = sqrt(arr.map(x => pow(x - mean, 2)).reduce((a, b) => a + b, 0) / len);
  let stdv_pct = stdv / mean * 100

  // rounding
  mean = ~~(mean * 100) / 100;
  median = ~~(median * 100) / 100;
  stdv = ~~(stdv * 100) / 100;
  stdv_pct = ~~(stdv_pct * 100) / 100;

  if (!mean_only)
    return { mean, median, stdv, stdv_pct };
  else
    return mean;
};


const getBackend = async (name: string) => {
  console.log(`Getting ${name}`);
  const url = `https://api-qcon.quantum-computing.ibm.com/api/Backends/${name}/properties`;
  let gates = (await GET(url))?.gates;

  const gate_times = new Map();

  for (const gate of gates) {
    if (gate_times.has(gate.gate)) {
      const updated = gate_times.get(gate.gate)

      updated.push(gate.parameters.find(x => x.name === "gate_length")?.value || 0)
      gate_times.set(gate.gate, updated);
    } else {
      gate_times.set(gate.gate, [gate.parameters?.find(x => x.name === "gate_length")?.value || 0]);
    }
  }

  for (const [key, value] of gate_times.entries())
    gate_times.set(key, stats(value, true));

  return {
    name,
    gate_times: Object.fromEntries(gate_times)
  };
};

let data: Promise<any> | any = await Promise.all(names.map(getBackend));
data = JSON.stringify(data, null, 2);

if (typeof Bun !== "undefined")
  Bun.write("times.json", data);
else
  fs.writeFileSync("times.json", data);