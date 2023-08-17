from math import sqrt
from random import randint
from time import sleep
from os import remove
import sys

DATA_FILE = "./data/spingrid.csv"
LOSS_FILE = "./data/convergence.csv"

SAFETY_CUTOFF = 100

def rand():
  return str(randint(0, 1))

# MAIN
def generate_values(n):
  result = ""

  for x in range(n+1):
    for y in range(n+1):
      result += rand()
      if y < n:
        result += ","
    result += "\n"

  return result

def calculate_loss(n):
  result = ""
  for x in range(100-n):
    rt = sqrt(x)
    jitter = 0.25 * rt
    y = round(10 - rt + jitter, 2)
    result += str(x) + "," + str(y) + "\n"

  return result

# first delete .csv files
try:
  remove(DATA_FILE)
  remove(LOSS_FILE)
  print("Deleted old files")
except:
  print("No old files")

loops = SAFETY_CUTOFF
while loops > 0:
  print("Running loop " + str(loops))
  sleep(0.5)

  n = int(sys.argv[1])

  fp = open(DATA_FILE, "w")
  fp.write(generate_values(n))
  fp.close()

  fp2 = open(LOSS_FILE, "w")
  fp2.write(calculate_loss(loops))
  fp2.close()

  loops -= 1
  sleep(0.5)