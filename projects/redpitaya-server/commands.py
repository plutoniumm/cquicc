import sys
from time import sleep
import redpitaya_scpi as scpi

rp_s = scpi.scpi(sys.argv[1])

"""
LED:MMC - Orange LED | Memory Card LED
LED:HB - Red LED | Board Activity LED
LED:ETH - Ethernet LED
"""

# toggle led blink
def blink(interval:int, iters: int, led: int)->None:
  print("Blinking LED1")
  success = 0
  for _ in range(iters):
    sleep(interval)
    rp_s.tx_txt("DIG:PIN LED"+str(led)+",1")
    sleep(interval)
    rp_s.tx_txt("DIG:PIN LED"+str(led)+",0")

    success+=1
    print("Blinked", iters)

  if success == iters:
    print("Blinked LED"+str(led)+" "+str(iters)+" times")
    return True
  else:
    print("Failed to blink LED"+str(led))
    return False

# check if scpi server running
def check_scpi():
  print("Checking if SCPI server is running")
  try:
    rp_s.tx_txt("*IDN?")
    print("SCPI server is running")
    return True
  except:
    print("SCPI server is not running")
    return False