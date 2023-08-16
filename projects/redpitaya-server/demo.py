from math import sqrt
from random import randint
from time import sleep
from os import remove

DATA_FILE = "./data/send.txt"
LOSS_FILE = "./data/loss.txt"

SAFETY_CUTOFF = 100
ITERS = 50

# MAIN
ITERS = range(ITERS + 1)
def generate_values():
  result = ""

  for x in ITERS:
    for y in ITERS:
      RND = str(randint(0, 1))
      result += str(x) + "," + str(y) + "," + RND + "\n"

  return result

def calculate_loss(x):
  x = 100-x
  jitter = 0.25 * x
  y = round(10 - sqrt(x) + jitter, 2)

  return str(x) + "," + str(y) + "\n"

# first delete .txt files
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
    fp.write(generate_values())
    fp2.write(calculate_loss(loops))

    sleep(1)
    loops -= 1