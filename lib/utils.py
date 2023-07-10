def log(st): # blue
  print("LOG: \033[94m" + st + "\033[0m")

def timer(s,e): # green
  c = int((e-s)/6)/10; # min with 1 decimal
  st = "\033[92m" + str(c+1) + "min\033[0m"
  return st

def warn(st): # yellow
  print("WARNING: \033[93m" + st + "\033[0m")

def report(st): # green
  print("REPORT: \033[92m" + st + "\033[0m")