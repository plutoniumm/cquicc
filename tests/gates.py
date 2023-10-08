def H(qubit):
  if isinstance(qubit, int):
    return f'qc.h({qubit})'
  if isinstance(qubit, list):
    return f'qc.h({json.dumps(qubit)})'

def X(q):
  return f'qc.x({q})'

def Y(q):
  return f'qc.y({q})'

def Z(q):
  return f'qc.z({q})'

def RX(q, rad):
  return f'qc.rx({float(rad)}, {q})'

def RY(q, rad):
  return f'qc.ry({float(rad)}, {q})'

def RZ(q, rad):
  return f'qc.rz({float(rad)}, {q})'

def CX(c, t):
  return f'qc.cx({c}, {t})'

def CCX(c1, c2, t):
  return f'qc.ccx({c1}, {c2}, {t})'

# Define a nullgate function
def nullgate(_):
  return ''