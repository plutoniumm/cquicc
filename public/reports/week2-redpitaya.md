---
topic: "Redpitaya WebApp"
title: "Weekly Update"
author: "Manav Seksaria"
from: "MCQuICC, IIT Madras"
---

===

## Current State

As of [This commit](https://github.com/plutoniumm/cquicc/tree/b8b15d1d37487f90c463e0e48d8ad1ed6f64167f) the RedPitaya has a 'blink' function on the homepage which can run from anywhere (On the IITM network) and cause the Redpitaya to blink its LEDs 3 times at 0.5Hz. This follows from the [Documentation Example](https://redpitaya.readthedocs.io/en/latest/developerGuide/software/build/webapp/webexamples/addLEDbut.html) as agreed upon

**Caveats**:
- It currently assumes the SCPI Server is also running, which may not always be the case. I am working on a small fix where it will check if the SCPI server is running, and if not, it will start it without the end user having to do anything



/===