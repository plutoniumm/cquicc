from math import sqrt
from random import randint
from time import sleep
from os import remove

DATA_FILE = "./data/spingrid.csv"
LOSS_FILE = "./data/convergence.csv"

SAFETY_CUTOFF = 100

def rand():
  return str(randint(0, 1))

# MAIN
def generate_values(n):
  result = ""
  # create nxn binary matrix
  # format 1,0,1,1,0...1\n1,0,1...

  for x in range(n+1):
    for y in range(n+1):
      result += rand()
      if y < n:
        result += ","
    result += "\n"

  return result

def calculate_loss(x):
  x = 100-x
  rt = sqrt(x)
  jitter = 0.25 * rt
  y = round(10 - rt + jitter, 2)

  return str(x) + "," + str(y) + "\n"

# first delete .csv files
try:
  remove(DATA_FILE)
  remove(LOSS_FILE)
  print("Deleted old files")
except:
  print("No old files")

loops = SAFETY_CUTOFF
while loops > 0:
  with \
  open(DATA_FILE, "w") as fp, \
  open(LOSS_FILE, "a") as fp2:
    print("Running loop " + str(loops))
    fp.write(generate_values(25))
    fp2.write(calculate_loss(loops))

    loops -= 1
    fp.close()
    fp2.close()
    sleep(1)