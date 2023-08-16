from math import sqrt
from random import random
from time import sleep, time_ns

DATA_FILE = "./data/send.txt"
LOSS_FILE = "./data/loss.txt"

SAFETY_CUTOFF = 100
ITERS = 50

# MAIN
ITERS = range(ITERS + 1)
def generate_values():
  result = ""
  NUM = time_ns() % 32768

  for x in ITERS:
    for y in ITERS:
      NUM = ((NUM * 11345 + 12345) % 32768) // 100
      RND = str(NUM % 2)

      temp = str(x) + "," + str(y) + "," + RND + "\n"
      result += temp

  return result

def calculate_loss(x):
  jitter = (random() / 32768.0) * 0.1 * x
  y = round(sqrt(x) + jitter, 2)

  return "\n" + str(x) + "," + str(y)


loops = SAFETY_CUTOFF
while loops > 0:
  with \
  open(DATA_FILE, "w") as fp, \
  open(LOSS_FILE, "a") as fp2:
    fp.write(generate_values())
    fp2.write(calculate_loss(loops))

    sleep(1)
    loops -= 1