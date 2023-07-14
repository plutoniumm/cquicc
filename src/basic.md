---
topic: "QML: Week 1: 10th July - 14th July"
title: "Weekly Update"
author: "Manav Seksaria"
from: "MCQuICC, IIT Madras"
---

===

## QAOA Denoising
I built the QAOA and ran some preliminary tests on it, however it seems our Denoiser may not be suitable for it since:
- QAOA returns bit strings i.e individual states for each Qubit so say [1, 0, 1] or (Up, Down, Up) for 3 Qubits after the minimisation
- Our Denoiser on the other hand runs on probabilities of each state. So it operates on [0.25, 0.33, 0.66] or (25% Chance Up, 33% Up, 66% Up) for 3 Qubits

## Code Syntax Test
This is a test

```js
const host = `The below is a ${10/10} fail pattern`;
function test(a=" is ") {
  return (b="bad")=>{
    console.log("OOP" + a + b);
  }
}
test()(); // "OOP is bad"
```

There is some stuff I'm trying out Lorem ipsum dolor sit, amet consectetur adipisicing elit. Laboriosam repellat quae qui obcaecati ipsam sapiente sequi delectus minus dicta esse?

Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptates inventore laudantium, neque ad expedita voluptate voluptatibus dolorem tenetur, enim rerum ipsum ab nihil qui natus earum! Quas ad qui assumenda? Cupiditate perspiciatis itaque ipsa sit beatae consectetur vero. Ad, aliquid.

## This is a test
Lorem ipsum dolor sit, amet consectetur adipisicing elit. Laboriosam repellat quae qui obcaecati ipsam sapiente sequi delectus minus dicta esse?

# Math Test with Katex
Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi in ipsum iure est officia ut, excepturi rerum esse cum, delectus dolorem nam minima reiciendis.+++Quod accusantium commodi inventore ab enim eaque atque quidem maiores perferendis sequi! Laborum nobis voluptatem repellendus mollitia. Obcaecati, atotam dolorum odio itaque quas reprehenderit dicta iure laboriosam libero earum corrupti fugiat possimus pariatur rem, esse eos! Expedita veritatis facilis vel hic, soluta officia accusantium eum possimus cumque atque magnam aperiam voluptas, accusamus error, obcaecati laudantium.

$$
\begin{aligned}
\text{minimize} \quad & \sum_{i=1}^n \sum_{j=1}^n c_{ij} x_{ij} \\
\text{subject to} \quad & \sum_{i=1}^n x_{ij} = 1, \quad j=1,\ldots,n, \\
& \sum_{j=1}^n x_{ij} = 1, \quad i=1,\ldots,n, \\
& \sum_{i \in S} \sum_{j \in S} x_{ij} \le |S|-1, \quad \emptyset \subset S \subset \{1,\ldots,n\}, \\
& x_{ij} \in \{0,1\}, \quad i,j=1,\ldots,n.
\end{aligned}
$$

/===