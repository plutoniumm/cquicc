---
topic: "QML: Week 1: 10th July - 14th July"
title: "Weekly Update"
author: "Manav Seksaria,<br/>Supervisor: Prof. Anil Prabhakar"
from: "MCQuICC, IIT Madras"
---

===

## QAOA Denoising
I built the QAOA and ran some preliminary tests on it. However, it seems our Denoiser may not be suitable for it since:
- QAOA returns bit strings, i.e. individual states for each Qubit, so say [1, 0, 1] or (Up, Down, Up) for 3 Qubits after the minimisation
- Our Denoiser on the other hand, runs on probabilities of each state. So it operates on [0.25, 0.33, 0.66] or (25% Chance Up, 33% Up, 66% Up) for 3 Qubits

### Attempted Workaround (failed)
Trying to run by converting bitstrings to bitwise probabilities <br/>
  `QAOA Bitwise Values = (`\
&nbsp;&nbsp;`0.0000, 0.0000, 0.0000, 0.4667,`\
&nbsp;&nbsp;`0.5000, 0.5000, 0.4667, 0.4667`\
`)` \
  `Denoised Results = (`\
&nbsp;&nbsp;`0.0000, 0.0000, 0.0000, 0.1850,`\
&nbsp;&nbsp;`0.5650, 0.4826, 0.5259, 0.6184`\
`)`
  <br/>Results obtained were effectively all 0.5 since that is what we expected our model to do when we closed off the last session

  additionally, the _meaning_ of the results is very different for both the data types is very different. The QAOA outputs the exact state each Qubit will be in, whereas the AE is designed to run on data types which contain approximate probabilities or, in some sense, the information content of a given qubit.
+++
  Finally, even if all these issues were to be resolved, we know that summing is a non-reversible process, so when we go from `a+b = c`, we cannot start with `c` and conclude `a`, `b`.a'nd therefore, we cannot also reverse the qubitwise probability process to obtain the individual bitstrings.

### Conclusion
Barring the fact that the model is of poor quality & needs improvements, it is safe to conclude right now that we need a separate _kind_ of model if we intend to do denoising for a QAOA since the denoising has to be done at a much earlier stage and for a different data type.

## RedPitaya WebApp
A basic web server on Python & a display for it to communicate to is ready, everything else will be taken care of RedPitaya's Linux automatically.

Pending a little more discussion on the exact details of how it should work on Tuesday, I can then go ahead and make the UI & APIs for communication with the device. I'll keep the code as simple as possible so that the code can be maintained even without me.

**Gap**: Testing the server on the redpitaya itself since I don't havedon'tIIT Wifi login creds yet, so I can't connect it & my laptop has network ports blocked

/===