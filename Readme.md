<div align="center">
<img src="./assets/icon.svg" height="100px" width="100px" />
<h2> QSVM </h2>
</div>


| Structure | Desc |
| --- | --- |
| [/saidl](./saidl/result.json) | Reproduction of Sai's work |
| [root](./result.json) | LTI QSVM Vanilla |

```js
// Confusion Matrices
vanilla= [
 [16, 10],
 [ 5,  9]
]
zz_2x3=[
 [ 4, 22],
 [ 0, 14]
]
zz_3x2=[
 [ 7, 19],
 [ 3, 11]
]
```

### 1200
```log
LOG: Starting baseline Program with no Optimizations...
LOG: Circuits Created
Using: <IBMBackend('ibmq_qasm_simulator')> with Circuit Depth: 57 and 6 qubits
LOG: Starting Estimator on 384 jobs
LOG: Running Job: 120/384
LOG: Running Job: 384/384
training time:846.3min
[[1.         0.00195312 0.04101562 ... 0.01757812 0.00585938 0.00390625]
 [0.00195312 1.         0.09570312 ... 0.01953125 0.         0.02734375]
 [0.04101562 0.09570312 1.         ... 0.0234375  0.0078125  0.01171875]
 ...
 [0.01757812 0.01953125 0.0234375  ... 1.         0.02148438 0.03320312]
 [0.00585938 0.         0.0078125  ... 0.02148438 1.         0.02734375]
 [0.00390625 0.02734375 0.01171875 ... 0.03320312 0.02734375 1.        ]]
LOG: Testing SVM...
230400
[[1.         0.00195312 0.04101562 ... 0.01757812 0.00585938 0.00390625]
 [0.00195312 1.         0.09570312 ... 0.01953125 0.         0.02734375]
 [0.04101562 0.09570312 1.         ... 0.0234375  0.0078125  0.01171875]
 ...
 [0.01757812 0.01953125 0.0234375  ... 1.         0.02148438 0.03320312]
 [0.00585938 0.         0.0078125  ... 0.02148438 1.         0.02734375]
 [0.00390625 0.02734375 0.01171875 ... 0.03320312 0.02734375 1.        ]]
LOG: Starting Testimator on 192 jobs
LOG: Running Job: 192/192
testing time:381.3min
Shape of K_1:  (240, 960)
Report:  {'0.0': {'precision': 0.4818181818181818, 'recall': 0.42063492063492064, 'f1-score': 0.4491525423728814, 'support': 126.0}, '1.0': {'precision': 0.43846153846153846, 'recall': 0.5, 'f1-score': 0.4672131147540984, 'support': 114.0}, 'accuracy': 0.4583333333333333, 'macro avg': {'precision': 0.46013986013986014, 'recall': 0.46031746031746035, 'f1-score': 0.4581828285634899, 'support': 240.0}, 'weighted avg': {'precision': 0.46122377622377625, 'recall': 0.4583333333333333, 'f1-score': 0.45773131425395946, 'support': 240.0}}
 Matrix:  [[53 73]
 [57 57]]
LOG: Done at 09:52:23
```