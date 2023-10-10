---
topic: "Redpitaya WebApp"
author: "Manav Seksaria"
from: "MCQuICC, IIT Madras"
---

===

## Current State

As of [This commit](https://github.com/plutoniumm/cquicc/tree/b8b15d1d37487f90c463e0e48d8ad1ed6f64167f) the RedPitaya has a 'blink' function on the homepage which can run from anywhere (On the IITM network) and cause the Redpitaya to blink its LEDs 3 times at 0.5Hz. This follows from the [Documentation Example](https://redpitaya.readthedocs.io/en/latest/developerGuide/software/build/webapp/webexamples/addLEDbut.html) as agreed upon

**Caveats**:
- It currently assumes the SCPI Server is also running, which may not always be the case. I am working on a small fix where it will check if the SCPI server is running, and if not, it will start it without the end user having to do anything
- The webserver currently runs on User's own system due to the fact that the code is written for python3.9 but RedPitaya's Linux is based on 3.5. I am working on a fix for this as well, but it's proving to be tricky. It will get solved but for record we have tried the following
  - Updating Redpitaya Linux: Fails to boot since Python is a dependency for Ubuntu
  - Trying install a custom 3.9: Fails to compile, python on custom location must be built from source
  - Trying to downgrade the code to 3.5: Dependency issues, currently what is being tried

### Next Steps
As soon as the Python issue & SCPI AutoStart issue are fixed, I'll make the Matrix processing from CSV file endpoint, that can be done even +++now since we don't really need any of the core redpitaya functions and only need Python, for that but it would be a hack, I'd rather have the redpitaya working perfectly first

### Demo
![Before](https://i.imgur.com/ZC5aoto.png)

When the `Blink LED1` button is pressed it sends a command to the Device, blinks the Orange LED 3 times and returns Success.

![After](https://i.imgur.com/VKmv1dn.png)

Anyone present near the Redpitaya will see the orange LED blink

![After](https://i.imgur.com/MyD7tkG_d.png)


/===