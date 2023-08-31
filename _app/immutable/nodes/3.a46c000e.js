import{_ as M}from"../chunks/preload-helper.a4192956.js";import{s as V,p as A,f as w,a as I,g as k,h as j,A as S,c as T,d as y,j as p,k as R,i as q,x as b,B as $,C as x,D as O,o as W}from"../chunks/scheduler.c749afcf.js";import{S as z,i as B,f as F,b as H,d as N,m as U,a as Y,t as K,e as G}from"../chunks/index.745b745c.js";import{j as J,c as Q,m as X,d as Z,a as ee,C as te,g as ne,b as se,l as ae}from"../chunks/utils.5143e4c8.js";const re=`<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://manav.ch/atomic.css">

  <link rel="stylesheet" href="css/reveal.css">

  <script src="/reveal.js"><\/script>
  <script src="/basics.js"><\/script>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize( { securityLevel: 'antiscript', theme: "base" } );
    loop( () => mermaid.init( undefined, $$( '.mermaid' ) ) )
  <\/script>
  <script>
    loop( () => { } );
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
<\/script>
<style>
  body {
    background-color: #ccc;
  }

  .reveal .slides {
    background: #fff;
  }
</style>

</html>`,ie={mangle:!1,headerIds:!1},le=n=>{n=n.replaceAll("===",`
</section><section>
`);const[,s,...a]=n.split("---"),l=J.load(s.trim(),{json:!0});let r=`<section>
`+Q(a.join("---"),ie)+`
</section>`;console.log(r),r=re.replace("&head;","").replace("&body;",r);for(let i in l)r=r.replace(`&${i};`,l[i]);return{meta:l,html:r}};const{window:oe}=ne;function ce(n){let s,a,l="TogglePrint",r,i,h="Print",g,d,u,o,C,E,c,e,f,v;function L(t){n[6](t)}let D={lang:X({base:se,codeLanguages:ae,completeHTMLTags:!0}),theme:Z,basic:!0,styles:ee,lineWrapping:!0,placeholder:"Type some markdown here..."};return n[0]!==void 0&&(D.value=n[0]),o=new te({props:D}),A.push(()=>F(o,"value",L)),o.$on("change",n[2]),{c(){s=w("div"),a=w("div"),a.textContent=l,r=I(),i=w("div"),i.textContent=h,g=I(),d=w("main"),u=w("div"),H(o.$$.fragment),E=I(),c=w("iframe"),this.h()},l(t){s=k(t,"DIV",{class:!0,id:!0});var m=j(s);a=k(m,"DIV",{class:!0,"data-svelte-h":!0}),S(a)!=="svelte-cksdy8"&&(a.textContent=l),r=T(m),i=k(m,"DIV",{class:!0,"data-svelte-h":!0}),S(i)!=="svelte-1nctn6c"&&(i.textContent=h),m.forEach(y),g=T(t),d=k(t,"MAIN",{class:!0});var _=j(d);u=k(_,"DIV",{class:!0});var P=j(u);N(o.$$.fragment,P),P.forEach(y),E=T(_),c=k(_,"IFRAME",{id:!0,frameborder:!0,title:!0,style:!0,class:!0}),j(c).forEach(y),_.forEach(y),this.h()},h(){p(a,"class","rx10 ptr svelte-1mq3o48"),p(i,"class","rx10 ptr svelte-1mq3o48"),p(s,"class","f j-ar p-fix w-50 svelte-1mq3o48"),p(s,"id","funcs"),p(u,"class","editor svelte-1mq3o48"),p(c,"id","mfWHAT"),p(c,"frameborder","0"),p(c,"title","Editor Output"),R(c,"background","#888"),p(c,"class","svelte-1mq3o48"),p(d,"class","f fw svelte-1mq3o48")},m(t,m){q(t,s,m),b(s,a),b(s,r),b(s,i),q(t,g,m),q(t,d,m),b(d,u),U(o,u,null),b(d,E),b(d,c),n[7](c),e=!0,f||(v=[$(oe,"keyup",n[5]),$(a,"click",n[3]),$(i,"click",n[4])],f=!0)},p(t,[m]){const _={};!C&&m&1&&(C=!0,_.value=t[0],x(()=>C=!1)),o.$set(_)},i(t){e||(Y(o.$$.fragment,t),e=!0)},o(t){K(o.$$.fragment,t),e=!1},d(t){t&&(y(s),y(g),y(d)),G(o),n[7](null),f=!1,O(v)}}}function de(n,s,a){let l="",r,i,h;const g=(e,f=!0)=>{const{html:v}=le(e);f&&localStorage.setItem("cquicc-present",e),h.open(),h.write(v),h.close()},d=()=>{const e=l;if(i===e)return 0;i=e,g(e)};W(async()=>{h||(h=r.contentWindow.document);const e=new URLSearchParams(location.search).get("demo"),f=localStorage.getItem("cquicc-present");if(f&&!e)g(f),a(0,l=f);else{const v=(await M(()=>import("../chunks/basic.1b656fae.js"),[],import.meta.url)).default;g(v,!1),a(0,l=v)}document.title+=(-new Date).toString(36)});const u=()=>{const e=/print-pdf/g.test(location.search)?location.href.replace(/\?print-pdf/g,""):location.href+"?print-pdf";window.location.href=e},o=()=>{/print-pdf/g.test(location.search)&&window.frames[0].print()},C=e=>{e.key==="p"&&e.ctrlKey&&u()};function E(e){l=e,a(0,l)}function c(e){A[e?"unshift":"push"](()=>{r=e,a(1,r)})}return[l,r,d,u,o,C,E,c]}class he extends z{constructor(s){super(),B(this,s,de,ce,V,{})}}export{he as component};
