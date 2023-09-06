---
topic: "QSVM at MCQuICC"
---

### Received Dataset

<style>
table { border-collapse: collapse; }
tr { border: none; }
td,th {
  border-right: solid 1px #8888;
  border-left: solid 1px #8888;
  padding: 0.2em 0.5em;
}
th{
  border-bottom: solid 1px #8888;
}
</style>

|Coolant T|Fuel P|LOG(Engine rpm)|LOG(Lub oil P)|LOG(Coolant P)|lub oil T|Engine Condition|
|---|---|---|---|---|---|---|
|-0.7727|0.3442|0.4828|-0.2438|0.2430|0.5634|**1**|
|...|...|...|...|...|...|...|
|...|...|...|1200 rows|...|...|
|...|...|...|...|...|...|...|
|-0.0863|-0.0622|-0.3165|-0.2442|0.5177|0.0347|**0**|
===

### Objectives
- Classify engine condition
- Use SVM for classification
- Compare QSVM with classical SVM

<br />
<img src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Kernel_Machine.svg" height="200px" />
<div>Kernel Machine</div>

===

We want a more accurate curvy line for which we need to transform the feature space. This is where the kernel trick comes in.

<br /><br />

<div class="f j-ar">
<div>

- Go to a higher dimension
- Find a linear separator
- Project back to original space

More mathematically
- Find a feature map $\phi$ such that $\phi(x_i) \cdot \phi(x_j) = K(x_i, x_j)$
- Generate a kernel matrix $K$ such that $K_{ij} = K(x_i, x_j)$
- Find all support vectors i.e $\alpha_i \because \sum \alpha_i y_i = 0$
- Find the bias $b$ such that $y_i(\sum \alpha_i y_i K(x_i, x_j) + b) = 1$
- We can now predict $Y_{OUT} = \text{sign}(\sum \alpha_i y_i K(X_{IN}, x_j) + b)$

</div>
<div>
<iframe height="200" style="width: 100%;" data-show-tab-bar='no' scrolling="no" title="3D Scatter Plot with Plotly.js Charts" src="/embed/scatter.html" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
</iframe>
</div>

===

## Two Approaches

<div class="f j-ar">
<div>
<h3>Quantum Precomputed + Classical SGD</h3>

⚛ Quantum precomputed kernel <br/>
↓ <br/>
💻 Classical SGD

<p><br></p>

**Advantages**
- Better feature space
- More noise resistant

</div>
<div>
<h3>Classical RBF + Annealing</h3>

💻 Classical RBF kernel <br/>
↓ <br/>
⚛ Quantum Annealing for minima

<p><br></p>

**Advantages**
- More feasible on current hardware
- Faster

</div>

===

## Quantum Precomputed Kernel Mechanism

- Each Pair of rows ${}^NC_2$ of 6 features each is fed to a quantum circuit as 12 parameters

<img src="https://i.imgur.com/31B1GXr.png" alt="QSVM Citcuit with U & U<sup>T</sup>" url="Higgs analysis with quantum classifiers, Belis et. al." height="100px" />

```mermaid
graph LR
  R1["Row 1"] --> C["ZZFeatureMap <span style="opacity:0">AB</span>"]
  R2["Row 2"] --> C2["ZZFeatureMap<sup>-1</sup> <span style="opacity:0">AB</span>"]

  C & C2 --> Compose["Compose A"] --> M["Measure |0&rangle;<sup>n</sup> <span style="opacity:0">AB</span>"]
```

===

## QUBO Annealing Mechanism
<div style="min-height:50vh">

```mermaid
graph TB
  A["<div>
  Calculate RBF Kernel Matrix from <br/>
   <math display="block"><msup><mi>e</mi><mrow><mo>-</mo><mi>γ</mi><msup><mrow><mo>||</mo><mi>x1</mi><mo>-</mo><mi>x2</mi><mo>||</mo></mrow><mrow><mn>2</mn></mrow></msup></mrow></msup></math>
  </div>"] --> B["<div>
    Get cost function <br/>
    <math display="block"><mrow><mtable><mtr><mtd columnalign="right"><mrow><munder><mo movablelimits="true">min</mo><mi>λ</mi></munder><mspace width="4pt"></mspace><mi mathvariant="script">L</mi><mrow><mo stretchy="false">(</mo><mi>λ</mi><mo stretchy="false">)</mo></mrow></mrow></mtd><mtd columnalign="left"><mrow><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><msub><mi>λ</mi><mi>i</mi></msub><msub><mi>λ</mi><mi>j</mi></msub><msub><mi>x</mi><mi>i</mi></msub><msub><mi>x</mi><mi>j</mi></msub><msub><mi>y</mi><mi>i</mi></msub><msub><mi>y</mi><mi>j</mi></msub><mo>-</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>N</mi></munderover><msub><mi>λ</mi><mi>i</mi></msub><mspace width="2em"></mspace><msub><mi>λ</mi><mi>i</mi></msub><mo>,</mo><msub><mi>λ</mi><mi>j</mi></msub></mrow></mtd></mtr></mtable></mrow></math>
  </div>"]
  B --> C["<div>
    Convert to binary form <br/>
    <math display="block"><mrow><mtable><mtr><mtd columnalign="right"><mrow><munder><mo movablelimits="true">min</mo><mrow><mover accent="true"><mi>λ</mi><mo stretchy="false">^</mo></mover><mo>∈</mo><msup><mrow><mi mathvariant="double-struck">B</mi></mrow><mrow><mi mathvariant="italic">NK</mi></mrow></msup></mrow></munder><mspace width="4pt"></mspace><mi mathvariant="script">L</mi><mrow><mo stretchy="false">(</mo><mover accent="true"><mi>λ</mi><mo stretchy="false">^</mo></mover><mo stretchy="false">)</mo></mrow><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><msup><mrow><mover accent="true"><mi>λ</mi><mo stretchy="false">^</mo></mover></mrow><mi>T</mi></msup><msup><mrow><mi mathvariant="script">P</mi></mrow><mi>T</mi></msup><mrow><mo stretchy="false">(</mo><mi>K</mi><mo>⊙</mo><mi>Y</mi><msup><mi>Y</mi><mi>T</mi></msup><mo stretchy="false">)</mo></mrow><mi mathvariant="script">P</mi><mover accent="true"><mi>λ</mi><mo stretchy="false">^</mo></mover><mo>-</mo><msup><mrow><mover accent="true"><mi>λ</mi><mo stretchy="false">^</mo></mover></mrow><mi>T</mi></msup><msup><mrow><mi mathvariant="script">P</mi></mrow><mi>T</mi></msup><msub><mn>1</mn><mi>N</mi></msub><mspace width="2em"></mrow></mtd></mtr></mtable></mrow></math>
  </div>"]
  P["<div>
  Desired Precision (P)
  <math display="block"><mrow><mo>(1, 2, 4, 8)</mo></mrow></math>
  </div>"] --> D
  C --> D["Quantum Annealing <span style="opacity:0">ABC</span>"]
```

</div>

===

## Results

Legend

<div class="f j-ar mx-a" style="width:80%;color">
  <div class="f p10 rx5" style="background:#aaf;">
    Classical SVM
  </div>
  <div class="f p10 rx5" style="background:#faa;">
    Quantum Kernel
  </div>
  <div class="f p10 rx5" style="background:#faf;">
    Quantum Annealing
  </div>
  <div class="f p10 rx5" style="background:#afa;">
    Final Quantum Annealing
  </div>
</div>

<img src="/assets/lti-qsvm-stats.svg" style="max-height:50vh" />

===

## Results

We notice the following
- 6 Qubit ZZFeatureMap is the best
- It is not obvious if more data is better
- The theoretical maxima of accuracy is probably &lt;70% since across all kernels the best accuracy is 67%

===

## How to improve?

Data is timeseries

<div class="f j-ar mx-a" style="width:80%">

<style>
  .box{
    height: 300px;
    width: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    border-radius: 10px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  }
</style>

<div class="box" style="background:#aaf;">
  <img src="/assets/rnn.png" width="90px" alt="rnn"
    style="mix-blend-mode: multiply;"
  />
  <div>RNN</div>
</div>
<div class="box" style="background:#faa;">
  <img src="/assets/vqc.png" width="120px" alt="rnn"
    style="mix-blend-mode: multiply;"
  />
  <div>VQCs</div>
</div>
<div class="box" style="background:#faf;">
  <svg viewBox="0 0 32 32" height="90px" width="90px" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    <circle cx="14" cy="14" r="12" />
    <path d="M23 23 L30 30"  />
  </svg>
  <div>Come up with a Quantum Time Series Mechanism</div>
</div>
</div>