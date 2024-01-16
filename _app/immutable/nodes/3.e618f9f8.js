import{s as S,f as y,a as q,g as w,h as k,d as p,c as T,j as d,k as b,i as _,x as g,H as I,E,y as A,I as V,G as U,e as L,p as B,l as F,m as H,J as N}from"../chunks/scheduler.a5ae9e1b.js";import{S as P,i as j}from"../chunks/index.3dc89a8d.js";function D(o){return(o==null?void 0:o.length)!==void 0?o:Array.from(o)}var x=(o,t)=>{if(t=Symbol[o])return t;throw Error("Symbol."+o+" is not defined")},Z=function(o,t){this[0]=o,this[1]=t},M=o=>{var t=o[x("asyncIterator")],n=!1,r,e={};return t==null?(t=o[x("iterator")](),r=i=>e[i]=h=>t[i](h)):(t=t.call(o),r=i=>e[i]=h=>{if(n){if(n=!1,i==="throw")throw h;return h}return n=!0,{done:!1,value:new Z(new Promise(f=>{var l=t[i](h);if(!(l instanceof Object))throw TypeError("Object expected");f(l)}),1)}}),e[x("iterator")]=()=>e,r("next"),"throw"in t?r("throw"):e.throw=i=>{throw i},"return"in t&&r("return"),e};function*O(o){let t=0;for(;t<o.length;)yield o[t++]}class m{constructor(t){if(this.data=[],Array.isArray(t))this.data=O(t);else if(t.constructor.name==="GeneratorFunction")this.data=t();else throw new Error("List constructor expects an array or a generator")}map(t,n){if(typeof t!="function")throw new TypeError("map expects a function");const r=this.data;return new m(function*(){let e=0;for(let i of r)yield t.call(n,i,e++,this)})}filter(t,n){if(typeof t!="function")throw new TypeError("filter expects a function");const r=this.data;return new m(function*(){let e=0;for(let i of r)t.call(n,i,e++,this)&&(yield i)})}forEach(t,n){if(typeof t!="function")throw new TypeError("forEach expects a function");let r=0;const e=this.data;return new m(function*(){for(let i of e)t.call(n,i,r++,this),yield i})}reduce(t,n){if(typeof t!="function")throw new TypeError("reduce expects a function");let r=0,e,i=this.data.next();if(i.done){if(n===void 0)throw new TypeError("reduce of empty list with no initial value");return n}for(n?e=n:e=i.value;!i.done;)e=t.call(void 0,e,i.value,r,this),i=this.data.next();return e}flat(t=1){if(typeof t!="number")throw new TypeError("flat expects a number");const n=this.data;return new m(function*(){for(let r of n)Array.isArray(r)&&t>0?yield*M(new m(r).flat(t-1).data):yield r})}collect(){return this.reduce((t,n)=>(t.push(n),t),[])}}const K=`Y1pYhoO::H,measure
l0plVKB::noise
ttgK6jg::Fake Simulator,code
UGfMGlr::Repeating H block
I5zO9AU::4 qubit gate-cut
00LQVIS::4 qubit gate-cut A
LRjtDEs::4 qubit gate-cut B
Fx9255F::5 qubit wire-cut
lQ4nYpe::5 qubit wire-cut,move gate
CtpoLhH::5 qubit wire-cut A
VDpMFgX::5 qubit wire-cut B
2DzzZP6::2 qubit gate decomposition
dTLoA8w::Abrax,4 qubit, GHZ,code
FnH21dT::4 qubit, GHZ
P4zZjy1::pauliList,code
nxk3L4d::partition problem,code
Xf1eDCN::code,generate subexperiments
doLg9Nn::code,run subexperiments
yv6i2ek::reconstruction,code
31B1GXr::UUt
igphC2o::teleportation,gate decomposition
LWcfCdQ::penrose notation svd
7K1yCgi::penrose notation circuit
vqAgDbH::zzfeaturemap map test
ZC5aoto::redpitaya,blink
VKmv1dn::redpitaya,blink
MyD7tkG_d::redpitaya board
tCxstBv::hydrogen,hartree fock,uncut
ohzXm7i::hydrogen,hartree fock,cut move
viadZ5M::hydrogen,hartree fock,cut A
PKUEFDp::hydrogen,hartree fock,cut B
Wwu9feU::hartree fock,hydrogen,chart,uncut
TwU0SiJ::hartree fock,hydrogen,chart,uncut
4aupdYs::hartree fock,hydrogen,chart,uncut
OnSPObf::hartree fock,hydrogen,chart,uncut, combined
4VFuYQB::hartree fock,hydrogen,chart,cut
LhCzQwZ::hartree fock,hydrogen,chart,cut
N1muvmn::hartree fock,hydrogen,chart,cut
T6qqVmr::hartree fock,hydrogen,chart,cut, combined`;function z(o,t,n){const r=o.slice();return r[8]=t[n],r}function C(o){let t,n,r,e,i,h=o[8][0]+"",f,l;return{c(){t=y("div"),n=y("img"),e=q(),i=y("div"),f=F(h),l=q(),this.h()},l(c){t=w(c,"DIV",{class:!0});var s=k(t);n=w(s,"IMG",{class:!0,src:!0,alt:!0}),e=T(s),i=w(s,"DIV",{class:!0});var a=k(i);f=H(a,h),a.forEach(p),l=T(s),s.forEach(p),this.h()},h(){d(n,"class","rx5 ptr svelte-i1tc4w"),N(n.src,r=o[8][1])||d(n,"src",r),d(n,"alt",o[8][0]),d(i,"class","p5 tc link svelte-i1tc4w"),d(t,"class","p5")},m(c,s){_(c,t,s),g(t,n),g(t,e),g(t,i),g(i,f),g(t,l)},p:A,d(c){c&&p(t)}}}function G(o){let t=o[2](o[0],o[8][0]),n,r=t&&C(o);return{c(){r&&r.c(),n=L()},l(e){r&&r.l(e),n=L()},m(e,i){r&&r.m(e,i),_(e,n,i)},p(e,i){i&5&&(t=e[2](e[0],e[8][0])),t?r?r.p(e,i):(r=C(e),r.c(),r.m(n.parentNode,n)):r&&(r.d(1),r=null)},d(e){e&&p(n),r&&r.d(e)}}}function Q(o){let t,n,r,e,i,h,f=D(o[3]),l=[];for(let c=0;c<f.length;c+=1)l[c]=G(z(o,f,c));return{c(){t=y("div"),n=y("input"),r=q(),e=y("div");for(let c=0;c<l.length;c+=1)l[c].c();this.h()},l(c){t=w(c,"DIV",{id:!0,class:!0,style:!0});var s=k(t);n=w(s,"INPUT",{type:!0,placeholder:!0,class:!0}),s.forEach(p),r=T(c),e=w(c,"DIV",{class:!0,style:!0});var a=k(e);for(let u=0;u<l.length;u+=1)l[u].l(a);a.forEach(p),this.h()},h(){d(n,"type","text"),d(n,"placeholder","Search"),d(n,"class","rx5 p10 d-b mx-a w-50 svelte-i1tc4w"),d(t,"id","search"),d(t,"class","p5 m5 p-fix svelte-i1tc4w"),b(t,"background","#fff"),b(t,"top","-5px"),b(t,"z-index","1"),d(e,"class","f j-ar fw"),b(e,"z-index","0"),b(e,"padding-top","100px")},m(c,s){_(c,t,s),g(t,n),I(n,o[0]),o[6](n),_(c,r,s),_(c,e,s);for(let a=0;a<l.length;a+=1)l[a]&&l[a].m(e,null);i||(h=[E(window,"keyup",o[4]),E(n,"input",o[5]),E(e,"click",Y)],i=!0)},p(c,[s]){if(s&1&&n.value!==c[0]&&I(n,c[0]),s&13){f=D(c[3]);let a;for(a=0;a<f.length;a+=1){const u=z(c,f,a);l[a]?l[a].p(u,s):(l[a]=G(u),l[a].c(),l[a].m(e,null))}for(;a<l.length;a+=1)l[a].d(1);l.length=f.length}},i:A,o:A,d(c){c&&(p(t),p(r),p(e)),o[6](null),V(l,c),i=!1,U(h)}}}function Y({target:o}){o.tagName==="IMG"&&navigator.clipboard.writeText(o.src)}function X(o,t,n){let r,e,i="";const h=new m(K.split(`
`)).filter(Boolean).map(a=>{let[u,v]=a.split("::");return u.includes("i.imgur")||(u=`https://i.imgur.com/${u}.png`),[v||u,u]}).collect();function f(a){return a.toLowerCase()}function l({key:a}){if(document.activeElement.tagName!=="INPUT")return a==="/"&&e.focus(),!0}function c(){i=this.value,n(0,i)}function s(a){B[a?"unshift":"push"](()=>{e=a,n(1,e)})}return n(2,r=(a,u)=>{if(a.length<2)return!0;u=f(u),a=f(a).replaceAll(" ",",").split(",");for(let v=0;v<a.length;v++)if(u.includes(a[v]))return!0;return!1}),[i,e,r,h,l,c,s]}class W extends P{constructor(t){super(),j(this,t,X,Q,S,{})}}export{W as component};
