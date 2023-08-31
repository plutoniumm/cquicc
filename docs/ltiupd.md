---
topic: "LTI Current State"
author: "Manav Seksaria,<br/>Supervisor: Prof. Anil Prabhakar"
from: "MCQuICC, IIT Madras"
---

# Problem Statement
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

| Test | Train | Accuracy | Run by | Source |
| --- | --- | --- | --- | --- |
| 900 | 300 | 0.65 | LTIM | `.xlsx` $\in$ Email@1/8/23 |
| 960 | 240 | 0.63 | CQuICC | Run on 29/8/23 |
| 160 | 40 | 0.5 | CQuICC | Run on 29/8/23 |

As we can see from here both 200 rows and 1200 rows have perfectly random and marginally better than random accuracy respectively

### Simulated QSVM
Using a simulated QSVM, where Ideal Quantum Simulator to create the precomputed kernel matrix, we get the following results

| Test | Train | Accuracy | Run by | Source |
| --- | --- | --- | --- | --- |
| 150 | 50 | 0.5 | LTIM | `.xlsx` $\in$ Email@1/8/23 |
| 150 | 50 | 0.42 | LTIM Run 2 | `.ipynb` $\in$ Message@25/8/23 |
| | | | | *All run on 24/8/23* |
| 160 | 40 | 0.63 | CQuICC | `6-ZZFeatureMap` |
| 160 | 40 | 0.45 | CQuICC | `2-ZZFeatureMap*3` |
| 160 | 40 | 0.45 | CQuICC | `3-ZZFeatureMap*2` |
| 960 | 240 | X | CQuICC | `6-ZZ` run on 29/8/23 |

### Real QSVM
No runs. We got terminated

### Simulated QUBO



### Real QUBO
No runs necessary. Not viable


## Conclusions






<!-- PARTH XLSX -->
| Type | Test | Train | Accuracy |
| --- | --- | --- | --- |
| SVM - RBF | 900 | 300 | 0.6466 |
| Logistic Regression | 900 | 300 | 0.6633 |
| Naive Bayes Classifier | 900 | 300 | 0.6282 |
| QSVM | 150 | 50 | 0.5 |
| QSVM Run 2 | 150 | 50 | 0.42 |