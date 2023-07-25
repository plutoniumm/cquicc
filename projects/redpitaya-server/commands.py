import sys
from time import sleep
import redpitaya_scpi as scpi

scpi_uri = sys.argv[1];
print("Connecting to: ", scpi_uri);
rp_s = scpi.scpi(scpi_uri);

"""
LED:MMC - Orange LED | Memory Card LED
LED:HB - Red LED | Board Activity LED
LED:ETH - Ethernet LED
"""

# toggle led blink
def blink(interval:int, iters: int, led: int)->None:
  print("Blinking LED1")
  success = 0
  for i in range(iters):
    sleep(interval)
    rp_s.tx_txt("DIG:PIN LED"+str(led)+",1")
    sleep(interval)
    rp_s.tx_txt("DIG:PIN LED"+str(led)+",0")

    success+=1
    print("Blinked", i)

  if success == iters:
    return True
  else:
    print("Failed to blink LED"+str(led))
    return False