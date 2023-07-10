import names from "./names.json" assert {type: 'json'};
import fs from "fs";

const GET = (url: string, opts = {}): Promise<any> =>
  fetch(url, opts).then(res => res.json());

const { sqrt, pow } = Math;

declare const Bun: any;
interface Stat {
  mean: number;
  median: number;
  stdv: number;
  stdv_pct: number;
}

interface Backend {
  name: string;
  frac: Stat;
  T1: Stat;
  T2: Stat;
}

// mean, median, stdv
const stats = (arr: number[]): Stat => {
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

  return { mean, median, stdv, stdv_pct };
};


const getBackend = async (name: string): Promise<Backend> => {
  console.log(`Getting ${name}`);
  const url = `https://api-qcon.quantum-computing.ibm.com/api/Backends/${name}/properties`;
  const qubits = (await GET(url))?.qubits;

  // pull out {name:T1} and {name:T2} from each qubit
  let T1: number[] | Stat = [];
  let T2: number[] | Stat = [];
  let frac: number[] | Stat = [];
  for (let qubit of qubits) { // get all T1 & T2
    const t1 = qubit.find(({ name }) => name === "T1")?.value * 1000; // convert to ns
    const t2 = qubit.find(({ name }) => name === "T2")?.value * 1000; // convert to ns

    if (t1 === undefined || t2 === undefined) continue;

    T1.push(t1);
    T2.push(t2);
    frac.push(t2 / t1);
  };

  T1 = stats(T1);
  T2 = stats(T2);
  frac = stats(frac);

  console.log(`Got ${name}`);
  return {
    name, frac,
    T1, T2,
  }
};

let data: Promise<any> | any = await Promise.all(names.map(getBackend));
data = JSON.stringify(data, null, 2);

if (typeof Bun !== "undefined")
  Bun.write("stats.json", data);
else
  fs.writeFileSync("stats.json", data);