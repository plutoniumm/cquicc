---
topic: "LTI Current State"
author: "Manav Seksaria"
from: "MCQuICC, IIT Madras"
---
===

## Problem Statement
LTI has given a dataset with 6 features of 200 rows and 1 feature which is the be the prediction for the same. This makes it a 7x200 dataset

Currently we're using QSVM to this and the following is the current state of it

## State
Index
- Classical SVM
- Simulated QSVM
- Real QSVM
- Simulated QUBO
- Real QUBO

### Classical SVM
Using a classical SVM with RBF Kernel, we get the following results

| Test | Train | Accuracy | Source |
| --- | --- | --- | --- |
| 900 | 300 | 0.65 | LTIM `.xlsx`* |
| 960 | 240 | 0.63 | `classical.py` |
| 160 | 40 | 0.5 | `classical.py` |

*Email dated 1/8/23

As we can see from here both 200 rows and 1200 rows have perfectly random and marginally better than random accuracy respectively

### Simulated QSVM
Using a simulated QSVM, where Ideal Quantum Simulator to create the precomputed kernel matrix, we get the following results
+++
| Test | Train | Accuracy | Source |
| --- | --- | --- | --- |
| 150 | 50 | 0.5 | LTIM `.xlsx`* |
| 150 | 50 | 0.42 | `assets/lti200.pdf` |
| | | | *Run by CQuICC* |
| 160 | 40 | 0.63 | `6-ZZFeatureMap` |
| 160 | 40 | 0.45 | `2-ZZFeatureMap*3` |
| 160 | 40 | 0.45 | `3-ZZFeatureMap*2` |
| 960 | 240 | 0.46 | `6-ZZFeatureMap` |

### Real QSVM
No runs. We got terminated

### Simulated QUBO
All of the following were run by CQuICC on 29/8/23 and logs are in the repository

| Test | Train | Accuracy | Sigma |
| --- | --- | --- | --- |
| 960 | 240 | 0.63 | 10 |
| 960 | 240 | 0.63 | 20 |
| 960 | 240 | 0.63 | 50 |
| 960 | 240 | 0.63 | 100 |
| 960 | 240 | 0.63 | 200 |


### Real QUBO
No runs necessary. Not viable


## Conclusions
/===