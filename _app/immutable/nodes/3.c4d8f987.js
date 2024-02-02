import{s as C,f as y,a as A,g as w,h as k,d as p,c as I,j as d,k as b,i as _,x as g,H as q,E as x,y as T,I as H,G as N,e as L,p as S,l as U,m as V,J as j}from"../chunks/scheduler.a5ae9e1b.js";import{S as F,i as P}from"../chunks/index.3dc89a8d.js";function D(o){return(o==null?void 0:o.length)!==void 0?o:Array.from(o)}var E=(o,t)=>{if(t=Symbol[o])return t;throw Error("Symbol."+o+" is not defined")},Z=function(o,t){this[0]=o,this[1]=t},K=o=>{var t=o[E("asyncIterator")],n=!1,r,e={};return t==null?(t=o[E("iterator")](),r=i=>e[i]=h=>t[i](h)):(t=t.call(o),r=i=>e[i]=h=>{if(n){if(n=!1,i==="throw")throw h;return h}return n=!0,{done:!1,value:new Z(new Promise(f=>{var l=t[i](h);if(!(l instanceof Object))throw TypeError("Object expected");f(l)}),1)}}),e[E("iterator")]=()=>e,r("next"),"throw"in t?r("throw"):e.throw=i=>{throw i},"return"in t&&r("return"),e};function*M(o){let t=0;for(;t<o.length;)yield o[t++]}class m{constructor(t){if(this.data=[],Array.isArray(t))this.data=M(t);else if(t.constructor.name==="GeneratorFunction")this.data=t();else throw new Error("List constructor expects an array or a generator")}map(t,n){if(typeof t!="function")throw new TypeError("map expects a function");const r=this.data;return new m(function*(){let e=0;for(let i of r)yield t.call(n,i,e++,this)})}filter(t,n){if(typeof t!="function")throw new TypeError("filter expects a function");const r=this.data;return new m(function*(){let e=0;for(let i of r)t.call(n,i,e++,this)&&(yield i)})}forEach(t,n){if(typeof t!="function")throw new TypeError("forEach expects a function");let r=0;const e=this.data;return new m(function*(){for(let i of e)t.call(n,i,r++,this),yield i})}reduce(t,n){if(typeof t!="function")throw new TypeError("reduce expects a function");let r=0,e,i=this.data.next();if(i.done){if(n===void 0)throw new TypeError("reduce of empty list with no initial value");return n}for(n?e=n:e=i.value;!i.done;)e=t.call(void 0,e,i.value,r,this),i=this.data.next();return e}flat(t=1){if(typeof t!="number")throw new TypeError("flat expects a number");const n=this.data;return new m(function*(){for(let r of n)Array.isArray(r)&&t>0?yield*K(new m(r).flat(t-1).data):yield r})}collect(){return this.reduce((t,n)=>(t.push(n),t),[])}}const Q=`Y1pYhoO::H,measure
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
HuiIJAr::hartree fock,hydrogen,chart,uncut, combined
4VFuYQB::hartree fock,hydrogen,chart,cut
LhCzQwZ::hartree fock,hydrogen,chart,cut
N1muvmn::hartree fock,hydrogen,chart,cut
InjhQpT::hartree fock,hydrogen,chart,cut, combined
5E21ITb::cut subexperiment, cut A
17op9sR::cut subexperiment, cut B
2E1BNG5::rxx
KHRn9pq::rxx,decomposition`;function G(o,t,n){const r=o.slice();return r[8]=t[n],r}function z(o){let t,n,r,e,i,h=o[8][0]+"",f,l;return{c(){t=y("div"),n=y("img"),e=A(),i=y("div"),f=U(h),l=A(),this.h()},l(a){t=w(a,"DIV",{class:!0});var s=k(t);n=w(s,"IMG",{class:!0,src:!0,alt:!0}),e=I(s),i=w(s,"DIV",{class:!0});var c=k(i);f=V(c,h),c.forEach(p),l=I(s),s.forEach(p),this.h()},h(){d(n,"class","rx5 ptr svelte-i1tc4w"),j(n.src,r=o[8][1])||d(n,"src",r),d(n,"alt",o[8][0]),d(i,"class","p5 tc link svelte-i1tc4w"),d(t,"class","p5")},m(a,s){_(a,t,s),g(t,n),g(t,e),g(t,i),g(i,f),g(t,l)},p:T,d(a){a&&p(t)}}}function B(o){let t=o[2](o[0],o[8][0]),n,r=t&&z(o);return{c(){r&&r.c(),n=L()},l(e){r&&r.l(e),n=L()},m(e,i){r&&r.m(e,i),_(e,n,i)},p(e,i){i&5&&(t=e[2](e[0],e[8][0])),t?r?r.p(e,i):(r=z(e),r.c(),r.m(n.parentNode,n)):r&&(r.d(1),r=null)},d(e){e&&p(n),r&&r.d(e)}}}function Y(o){let t,n,r,e,i,h,f=D(o[3]),l=[];for(let a=0;a<f.length;a+=1)l[a]=B(G(o,f,a));return{c(){t=y("div"),n=y("input"),r=A(),e=y("div");for(let a=0;a<l.length;a+=1)l[a].c();this.h()},l(a){t=w(a,"DIV",{id:!0,class:!0,style:!0});var s=k(t);n=w(s,"INPUT",{type:!0,placeholder:!0,class:!0}),s.forEach(p),r=I(a),e=w(a,"DIV",{class:!0,style:!0});var c=k(e);for(let u=0;u<l.length;u+=1)l[u].l(c);c.forEach(p),this.h()},h(){d(n,"type","text"),d(n,"placeholder","Search"),d(n,"class","rx5 p10 d-b mx-a w-50 svelte-i1tc4w"),d(t,"id","search"),d(t,"class","p5 m5 p-fix svelte-i1tc4w"),b(t,"background","#fff"),b(t,"top","-5px"),b(t,"z-index","1"),d(e,"class","f j-ar fw"),b(e,"z-index","0"),b(e,"padding-top","100px")},m(a,s){_(a,t,s),g(t,n),q(n,o[0]),o[6](n),_(a,r,s),_(a,e,s);for(let c=0;c<l.length;c+=1)l[c]&&l[c].m(e,null);i||(h=[x(window,"keyup",o[4]),x(n,"input",o[5]),x(e,"click",O)],i=!0)},p(a,[s]){if(s&1&&n.value!==a[0]&&q(n,a[0]),s&13){f=D(a[3]);let c;for(c=0;c<f.length;c+=1){const u=G(a,f,c);l[c]?l[c].p(u,s):(l[c]=B(u),l[c].c(),l[c].m(e,null))}for(;c<l.length;c+=1)l[c].d(1);l.length=f.length}},i:T,o:T,d(a){a&&(p(t),p(r),p(e)),o[6](null),H(l,a),i=!1,N(h)}}}function O({target:o}){o.tagName==="IMG"&&navigator.clipboard.writeText(o.src)}function R(o,t,n){let r,e,i="";const h=new m(Q.split(`
`)).filter(Boolean).map(c=>{let[u,v]=c.split("::");return u.includes("i.imgur")||(u=`https://i.imgur.com/${u}.png`),[v||u,u]}).collect();function f(c){return c.toLowerCase()}function l({key:c}){if(document.activeElement.tagName!=="INPUT")return c==="/"&&e.focus(),!0}function a(){i=this.value,n(0,i)}function s(c){S[c?"unshift":"push"](()=>{e=c,n(1,e)})}return n(2,r=(c,u)=>{if(c.length<2)return!0;u=f(u),c=f(c).replaceAll(" ",",").split(",");for(let v=0;v<c.length;v++)if(u.includes(c[v]))return!0;return!1}),[i,e,r,h,l,a,s]}class W extends F{constructor(t){super(),P(this,t,R,Y,C,{})}}export{W as component};
