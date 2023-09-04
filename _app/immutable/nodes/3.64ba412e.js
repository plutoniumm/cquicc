import{_ as re}from"../chunks/preload-helper.a4192956.js";import{s as le,p as H,f as _,a as I,e as U,g,h as D,A as R,c as S,d as u,j as p,i as j,x as h,B as V,C as X,D as ne,o as ie,k as N,E as Y}from"../chunks/scheduler.3fe22ecb.js";import{S as oe,i as ce,f as F,b as K,d as W,m as J,a as Q,t as Z,e as ee}from"../chunks/index.a14d807c.js";import{j as de,c as me,m as pe,d as ue,a as fe,C as he,R as ve,g as _e,b as ge,l as ke}from"../chunks/utils.48a973b1.js";const ye=`<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://manav.ch/atomic.css">

  <link rel="stylesheet" href="css/reveal.css">
  <link rel="stylesheet" href="css/revealmod.css">

  <script src="/reveal.js"><\/script>
  <script src="/basics.js"><\/script>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize( { securityLevel: 'antiscript', theme: "base" } );
    loop( () => {
      mermaid.init( undefined, $$( '.mermaid' ) )

      // extract all mermaids SVG
      const svgs = $$( '.mermaid svg' );
    } )
  <\/script>
  <script>
    if ( window.location.search.match( /print-pdf/gi ) ) {
      var link = document.createElement( 'link' );
      link.rel = 'stylesheet';
      link.type = 'text/css';
      link.href = 'css/pdf.css';
      document.getElementsByTagName( 'head' )[ 0 ].appendChild( link );
    }
  <\/script>
  &head;
</head>

<body vars='&vars;' xmlns="http://www.w3.org/2000/svg">
  <main class="reveal">
    <article class="slides">
      <section>
        <h2>&topic;</h2>
      </section>
      &body;
    </article>
  </main>
</body>

<script>
  Reveal.initialize();
  Reveal.slide( localStorage.getItem( 'currslide' ) || 0 );
  Reveal.addEventListener( 'slidechanged', ( e ) => {
    localStorage.setItem( 'currslide', e.indexh );
  } );
<\/script>
<style class="killCSS">
  body {
    background-color: #ccc;
  }

  .reveal .slides {
    background: #fff;
  }
</style>

</html>`,be={mangle:!1,headerIds:!1},we=a=>{const[,n,...t]=a.split("---"),r=de.load(n.trim(),{json:!0});let s=t.join("---").split("===").map(l=>me(l,be)).join("</section><section data-auto-animate>");s=ye.replace("&head;","").replace("&body;",`<section data-auto-animate>${s}</section>`);for(let l in r)s=s.replace(`&${l};`,r[l]);return{meta:r,html:s}},Ce=a=>(a.querySelectorAll(".killCSS").forEach(t=>t.remove()),`<head><script src="/reveal.js"><\/script>
<link rel="stylesheet" href="https://manav.ch/atomic.css">
<link rel="stylesheet" href="/css/reveal.css">
<link rel="stylesheet" href="/css/revealmod.css"></head><body>`+a.innerHTML+"</body>");const{window:xe}=_e;function te(a){let n,t,r,s,l="X",k,b;return{c(){n=_("div"),t=_("textarea"),r=I(),s=_("button"),s.textContent=l,this.h()},l(i){n=g(i,"DIV",{class:!0,id:!0});var m=D(n);t=g(m,"TEXTAREA",{name:!0,class:!0}),D(t).forEach(u),r=S(m),s=g(m,"BUTTON",{class:!0,style:!0,"data-svelte-h":!0}),R(s)!=="svelte-1l4u4xv"&&(s.textContent=l),m.forEach(u),this.h()},h(){p(t,"name","code"),p(t,"class","rpm-10 flow-y-s svelte-dn8k4i"),p(s,"class","d-b rx20 mx-a ptr"),N(s,"color","#fff"),N(s,"background","#f00"),N(s,"width","50px"),p(n,"class","p-fix blur tc svelte-dn8k4i"),p(n,"id","popup")},m(i,m){j(i,n,m),h(n,t),Y(t,a[1]),h(n,r),h(n,s),k||(b=[V(t,"input",a[9]),V(s,"click",a[10])],k=!0)},p(i,m){m&2&&Y(t,i[1])},d(i){i&&u(n),k=!1,ne(b)}}}function Ee(a){let n,t,r="TogglePrint",s,l,k="Print",b,i,m="GetCode",E,f,w,v,o,C,$,y,q,L,T,P,M,B;function se(e){a[7](e)}let O={lang:pe({base:ge,codeLanguages:ke,completeHTMLTags:!0}),extensions:[ue],basic:!0,styles:fe,lineWrapping:!0,placeholder:"Type some markdown here..."};a[0]!==void 0&&(O.value=a[0]),v=new he({props:O}),H.push(()=>F(v,"value",se));function ae(e){a[8](e)}let z={preprocess:a[2]};a[0]!==void 0&&(z.value=a[0]),y=new ve({props:z}),H.push(()=>F(y,"value",ae));let d=a[1].length&&te(a);return{c(){n=_("div"),t=_("div"),t.textContent=r,s=I(),l=_("div"),l.textContent=k,b=I(),i=_("div"),i.textContent=m,E=I(),f=_("main"),w=_("div"),K(v.$$.fragment),C=I(),$=_("div"),K(y.$$.fragment),L=I(),d&&d.c(),T=U(),this.h()},l(e){n=g(e,"DIV",{class:!0,id:!0});var c=D(n);t=g(c,"DIV",{class:!0,"data-svelte-h":!0}),R(t)!=="svelte-ui3179"&&(t.textContent=r),s=S(c),l=g(c,"DIV",{class:!0,"data-svelte-h":!0}),R(l)!=="svelte-199dnqx"&&(l.textContent=k),b=S(c),i=g(c,"DIV",{class:!0,"data-svelte-h":!0}),R(i)!=="svelte-30y22e"&&(i.textContent=m),c.forEach(u),E=S(e),f=g(e,"MAIN",{class:!0});var x=D(f);w=g(x,"DIV",{class:!0});var A=D(w);W(v.$$.fragment,A),A.forEach(u),C=S(x),$=g(x,"DIV",{class:!0});var G=D($);W(y.$$.fragment,G),G.forEach(u),x.forEach(u),L=S(e),d&&d.l(e),T=U(),this.h()},h(){p(t,"class","rx10 p10 ptr svelte-dn8k4i"),p(l,"class","rx10 p10 ptr svelte-dn8k4i"),p(i,"class","rx10 p10 ptr svelte-dn8k4i"),p(n,"class","f j-ar p-fix w-50 svelte-dn8k4i"),p(n,"id","funcs"),p(w,"class","editor svelte-dn8k4i"),p($,"class","frame svelte-dn8k4i"),p(f,"class","f fw svelte-dn8k4i")},m(e,c){j(e,n,c),h(n,t),h(n,s),h(n,l),h(n,b),h(n,i),j(e,E,c),j(e,f,c),h(f,w),J(v,w,null),h(f,C),h(f,$),J(y,$,null),j(e,L,c),d&&d.m(e,c),j(e,T,c),P=!0,M||(B=[V(xe,"keyup",a[5]),V(t,"click",a[3]),V(l,"click",a[4]),V(i,"click",a[6])],M=!0)},p(e,[c]){const x={};!o&&c&1&&(o=!0,x.value=e[0],X(()=>o=!1)),v.$set(x);const A={};!q&&c&1&&(q=!0,A.value=e[0],X(()=>q=!1)),y.$set(A),e[1].length?d?d.p(e,c):(d=te(e),d.c(),d.m(T.parentNode,T)):d&&(d.d(1),d=null)},i(e){P||(Q(v.$$.fragment,e),Q(y.$$.fragment,e),P=!0)},o(e){Z(v.$$.fragment,e),Z(y.$$.fragment,e),P=!1},d(e){e&&(u(n),u(E),u(f),u(L),u(T)),ee(v),ee(y),d&&d.d(e),M=!1,ne(B)}}}function $e(a,n,t){let r="",s="";const l=o=>{const{html:C}=we(o||"");return localStorage.setItem("cquicc-present",o),C};ie(async()=>{const o=localStorage.getItem("cquicc-present");if(o.length>1)t(0,r=o);else{const C=(await re(()=>import("../chunks/basic.1b656fae.js"),[],import.meta.url)).default;t(0,r=C)}document.title+=(-new Date).toString(36)});const k=()=>{const o=/print-pdf/g.test(location.search)?location.href.replace(/\?print-pdf/g,""):location.href+"?print-pdf";window.location.href=o},b=()=>{/print-pdf/g.test(location.search)&&window.frames[0].print()},i=o=>{o.key==="p"&&o.ctrlKey&&k()},m=()=>t(1,s=Ce(window.frames[0].document.body));function E(o){r=o,t(0,r)}function f(o){r=o,t(0,r)}function w(){s=this.value,t(1,s)}return[r,s,l,k,b,i,m,E,f,w,()=>t(1,s="")]}class De extends oe{constructor(n){super(),ce(this,n,$e,Ee,le,{})}}export{De as component};
