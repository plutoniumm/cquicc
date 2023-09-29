// nullgate "-"
function H (qubit) {
  if (typeof qubit === "number") {
    return `qc.h(${qubit})`;
  }
  if (Array.isArray(qubit)) {
    return `qc.h(${JSON.stringify(qubit)})`;
  };
}

export default {
  "-": (_) => ``,
  H,
  CX: (c, t) => `qc.cx(${c}, ${t})`,
  CCX: (c1, c2, t) => `qc.ccx(${c1}, ${c2}, ${t})`,

  X: (q) => `qc.x(${q})`,
  Y: (q) => `qc.y(${q})`,
  Z: (q) => `qc.z(${q})`,

  RX: (q, rad) => `qc.rx(${parseFloat(rad)}, ${q})`,
  RY: (q, rad) => `qc.ry(${parseFloat(rad)}, ${q})`,
  RZ: (q, rad) => `qc.rz(${parseFloat(rad)}, ${q})`
}