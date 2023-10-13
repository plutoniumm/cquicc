---
topic: '<span style="font:700 1.5em Helvetica;">Ciruit Cutting</span>'
---

<link rel="stylesheet" href="https://quantumjavascript.app/Q/Q.css" />
<link rel="stylesheet" href="https://quantumjavascript.app/Q/Q-Circuit-Editor.css" />
<script src="https://quantumjavascript.app/Q/Q.js"></script>
<script src="https://quantumjavascript.app/Q/Q-ComplexNumber.js"></script>
<script src="https://quantumjavascript.app/Q/Q-Matrix.js"></script>
<script src="https://quantumjavascript.app/Q/Q-Qubit.js"></script>
<script src="https://quantumjavascript.app/Q/Q-Gate.js"></script>
<script src="https://quantumjavascript.app/Q/Q-History.js"></script>
<script src="https://quantumjavascript.app/Q/Q-Circuit.js"></script>
<script src="https://quantumjavascript.app/Q/Q-Circuit-Editor.js"></script>

### Why Circuit Cutting?
Let us say we have the below circuit and it needs to be broken into smaller circuits. There are a few key reasons to do this

===

<h2>Large Circuits are noisy</h2>

<section data-transition="fade-in none-out">
<h3>What is noise?</h3>
<div class="f j-ar tc"><div>
<img src="https://i.imgur.com/Y1pYhoO.png" />
</div><div class="f j-ct al-ct"><span>
This should give us:<br/> <code class="d-b m20">50%: 0, 50%: 1</code>
</span></div></div>
<img src="https://i.imgur.com/l0plVKB.png" style="max-height:33vh;" class="fade-in fragment"/>
</section>

<section data-transition="none-in fade-out" style="overflow:hidden;">
<h3>What does noise look like?</h3>

It could be *heat*, *vibration*, *material imperections*, *stray electric fields* etc. We can statistically simulate this noise

<style>
table{ width:80%; }
td{ width:50%; }
tr{ width:100%; }
</style>

<div class="f j-ar tc"><div>
<img src="https://i.imgur.com/ttgK6jg.png" style="height:33vh;"/>
</div><div class="f j-ct al-ct">
<svg viewBox="0 0 216 250" style="height:33vh;">
  <path stroke="#b095ff" stroke-width="16" d="M166 190h-34"/>
  <path stroke="#5668ff" stroke-width="16" d="M50 190h34"/>
  <path stroke="#f2eff8" stroke-width="16" d="M108 132v34"/>
  <path stroke="#d5bdff" stroke-width="16" d="M108 84V50"/>
  <path stroke="#cdb4ff" stroke-width="16" d="M166 26h-34"/>
  <path stroke="#0f62fe" stroke-width="16" d="M50 26h34"/>
  <g transform="translate(26 26)">
    <circle r="24" fill="#dfccfd" stroke="#262626" stroke-width="2"/>
    <text fill="#161616" dy=".3em" text-anchor="middle">0</text>
  </g>
  <g transform="translate(108 26)">
    <circle r="24" fill="#f2eff8" stroke="#262626" stroke-width="2"/>
    <text fill="#161616" dy=".3em" text-anchor="middle">1</text>
  </g>
  <g transform="translate(190 26)">
    <circle r="24" fill="#9275ff" stroke="#262626" stroke-width="2"/>
    <text fill="#161616" dy=".3em" text-anchor="middle">2</text>
  </g>
  <g transform="translate(108 108)">
    <circle r="24" fill="#5b68ff" stroke="#262626" stroke-width="2"/>
    <text fill="#FFF" dy=".3em" text-anchor="middle">3</text>
  </g>
  <g transform="translate(26 190)">
    <circle r="24" fill="#a88dff" stroke="#262626" stroke-width="2"/>
    <text fill="#161616" dy=".3em" text-anchor="middle">4</text>
  </g>
  <g transform="translate(108 190)">
    <circle r="24" fill="#e4d6fc" stroke="#262626" stroke-width="2"/>
    <text fill="#161616" dy=".3em" text-anchor="middle">5</text>
  </g>
  <g transform="translate(190 190)">
    <circle r="24" fill="#0f62fe" stroke="#262626" stroke-width="2"/>
    <text fill="#FFF" dy=".3em" text-anchor="middle">6</text>
  </g>
  <text stroke="transparent" fill="#161616" x="100" y="240" text-anchor="middle">IBM Perth</text>
</svg>
</div></div>

</section>
<section data-transition="none-in fade-out" style="overflow:hidden;">
<div id="circuitCont" class="p-rel" style="min-height:10rem"></div>

<div class="f j-ar tc"><div>
<button id="l" class="rpm-10 aaf" onclick="edit(this)">&larr;</button>
</div>

Let's model some noise with this **1 Block**

<div>
<button id="r" class="rpm-10 aaf" onclick="edit(this)">&rarr;</button>
</div></div>

<pre id="report">
000
001
010
011
100
100
101
110
111
</pre>
<style>
.Q-circuit-header,
.Q-circuit-toolbar,
.Q-circuit p { display:none; }
#report{ transform: scale(0.75) translateY(-15%); }
</style>

<script>
let i = 0;
const versions = [
`X#0-I---I-
X#1-X#0-I-
I---X#1-I-`,
// with H
`X#0-I---I--H-
X#1-X#0-I--H-
I---X#1-I-H-`,
// repeat CNOT
`X#0-I---I---H-X#0-I---I-
X#1-X#0-I---H-X#1-X#0-I-
I---X#1-I---H-I---X#1-I-`,
// add H
`X#0-I---I---H-X#0-I---I---H-
X#1-X#0-I---H-X#1-X#0-I---H-
I---X#1-I-H-I---X#1-I-H-`,
];

function render(i){
    const cont = document.getElementById('circuitCont');
    const report = document.getElementById('report');
    const text = versions[i];

    const circuit = Q( text );
    const value = circuit.report$();

    cont.innerHTML = '';
    circuit.toDom(cont)
    report.innerHTML = value;
}
setTimeout(() => render(0), 1000);

function edit(el){
    i = i + (el.id == 'l' ? -1 : 1);
    i = i % versions.length;
    render(i);
}
</script>

</section>
<section data-transition="fade-in none-out">
<div class="f">
<img src="https://i.imgur.com/UGfMGlr.png" style="flex:1;object-fit:contain;max-width:33%;"/>
<pre>


 ..N times...

</pre>
<img src="https://i.imgur.com/YbD7ZBq.png" style="flex:1;object-fit:contain;max-width:33%;"/>
</div>
<iframe src="/embed/noise.html" style="width:80%;aspect-ratio:16/9" frameborder="0"></iframe>
</section>

===

<section data-transition="fade-in none-out">
<h2> Gate Cuts </h2>
<img src="https://i.imgur.com/I5zO9AU.png" />
</div>
</section>
<section data-transition="none-in fade-out">
<h2> Gate Cuts </h2>

<img src="https://i.imgur.com/00LQVIS.png">
<img src="https://i.imgur.com/LRjtDEs.png">

</section>

===

<section data-transition="fade-in none-out">
<h2> Wire Cuts </h2>
<img src="https://i.imgur.com/Fx9255F.png" />
</div>
</section>
<section data-transition="none-in fade-out">
<h2> Wire Cuts </h2>
<img src="https://i.imgur.com/lQ4nYpe.png">
</section>
<section data-transition="none-in fade-out">
<h2> Wire Cuts </h2>

<img src="https://i.imgur.com/CtpoLhH.png">
<img src="https://i.imgur.com/VDpMFgX.png">

</section>

===

### Sample Breakdown

<img src="https://i.imgur.com/2DzzZP6.png" style="max-width:100%"/>

### CZ Gate: $e^{-i\frac{\pi}{4} (I-Z_1)(I-Z_2)}$

<img src="https://i.imgur.com/m3nEnmc.png" style="max-width:100%"/>

lets do an actual problem

===

## Breaking 4-GHZ into two

<section data-transition="fade-in none-out">

1. Define our Circuit & its Observables
2. Define our Cuts
3. Determine Subexperiments & their weights
4. Run!
5. Do Stats & Compare results

<br/>

Luckily setps 2,3,5 are made easy by the Circuit Knitting Toolbox

</section><section data-transition="none-in fade-out">
<h3> 1. Define our Circuit & its Observables </h3>
<div class="f j-ar tc"><div>
    <img src="https://i.imgur.com/dTLoA8w.png" style="height:25vh"/>
</div><div>
    <img src="https://i.imgur.com/FnH21dT.png" style="height:25vh"/>
</div></div>

<img src="https://i.imgur.com/P4zZjy1.png" style="max-height:25vh;"/>

</section><section data-transition="none-in fade-out">
<h3> 2. Define our Cuts </h3>

<img src="https://i.imgur.com/nxk3L4d.png" style="max-height:28vh;"/>

<div class="f-col">
<img src="https://i.imgur.com/dV2ICTa.png" style="max-height:15vh;object-fit:contain;"/>
<img src="https://i.imgur.com/D1wlCTg.png" style="max-height:15vh;object-fit:contain;"/>

</section><section data-transition="none-in fade-out">
<h3> 3. Determine Subexperiments & their weights </h3>
<img src="https://i.imgur.com/Xf1eDCN.png" style="max-height:28vh;"/>

</section><section data-transition="none-in fade-out">
<h3> 4. Run! </h3>
<img src="https://i.imgur.com/doLg9Nn.png" style="max-height:50vh;"/>

</section><section data-transition="none-in fade-out">
<h3> 5. Do Stats & Compare results </h3>

<img src="https://i.imgur.com/yv6i2ek.png" style="max-height:33vh;"/>


<div class="f j-ar tc"><div>

Original Circ Values: <br/> $[1.0, 1.0, 1.0, 1.0]$

</div><div>

Reconstructed Values:<br/> $[0.9763, 1.0002, 0.9999, 1.0173]$

</div></div>
</section>

===

## Open Questions

- How can we still get similar results without high overhead
- What is the best cut? Horizontal? Vertical? Hybrid?
- How well can we generalize this idea at scale

<img src="https://qiskit-extensions.github.io/circuit-knitting-toolbox/_images/circuit_cutting_tutorials_01_gate_cutting_to_reduce_circuit_width_2_0.png" />

===

## Resources
- [1] ibm.com/quantum/roadmap
- Circuit Knitting Toolbox: *qiskit-extensions.github.io/circuit-knitting-toolbox*
- [2] [Mitarai & Fujii, *Constructing a virtual two-qubit gate by sampling single-qubit operations*](https://browse.arxiv.org/pdf/1909.07534.pdf)
- [3] CZ Expectation Replication: *pastebin.com/mY2AKBNp*

## Futher Reading

- Kosuke Mitarai, & Keisuke Fujii *Overhead for simulating a non-local channel with local channels by quasi-probability sampling*
- Lukas Brenner, Christophe Piveteau, & David Sutter. *Optimal wire cutting with classical communication*
Kristan Temme, Sergey Bravyi, & Jay M. Gambetta (2017). *Error Mitigation for Short-Depth Quantum Circuits*