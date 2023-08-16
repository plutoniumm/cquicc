from math import sqrt
from random import randint,random
from time import sleep, time_ns

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

      temp = str(x) + "," + str(y) + "," + RND + "\n"
      result += temp

  return result

def calculate_loss(x):
  jitter = (random() / 32768.0) * 0.1 * x
  y = round(sqrt(x) + jitter, 2)

  return str(x) + "," + str(y) + "\n"


loops = SAFETY_CUTOFF
while loops > 0:
  with \
  open(DATA_FILE, "w") as fp, \
  open(LOSS_FILE, "a") as fp2:
    fp.write(generate_values())
    fp2.write(calculate_loss(loops))

    sleep(1)
    loops -= 1