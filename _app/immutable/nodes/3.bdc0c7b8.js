import{_ as O}from"../chunks/preload-helper.a4192956.js";import{s as W,p as q,f as w,a as D,e as L,g as y,h as j,A as R,c as S,d as h,j as l,k as B,i as T,x as C,B as A,C as F,D as H,o as U,E as V}from"../chunks/scheduler.3fe22ecb.js";import{S as Y,i as K,f as X,b as G,d as J,m as Q,a as Z,t as ee,e as te}from"../chunks/index.a14d807c.js";import{j as ne,c as se,m as ae,d as ie,a as re,C as le,g as oe,b as ce,l as de}from"../chunks/utils.715bece7.js";const me=`<!DOCTYPE html>
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
    loop( () => mermaid.init( undefined, $$( '.mermaid' ) ) )
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
<style>
  body {
    background-color: #ccc;
  }

  .reveal .slides {
    background: #fff;
  }
</style>

</html>`,pe={mangle:!1,headerIds:!1},ue=i=>{const[,s,...e]=i.split("---"),r=ne.load(s.trim(),{json:!0});let o=e.join("---").split("===").map(t=>se(t,pe)).join("</section><section>");o=me.replace("&head;","").replace("&body;",`<section>${o}</section>`);for(let t in r)o=o.replace(`&${t};`,r[t]);return{meta:r,html:o}};const{window:fe}=oe;function M(i){let s,e,r,o;return{c(){s=w("div"),e=w("textarea"),this.h()},l(t){s=y(t,"DIV",{class:!0,id:!0});var u=j(s);e=y(u,"TEXTAREA",{name:!0,id:!0,width:!0,height:!0,class:!0}),j(e).forEach(h),u.forEach(h),this.h()},h(){l(e,"name","code"),l(e,"id",""),l(e,"width","80%"),l(e,"height","80%"),l(e,"class","rpm-10"),l(s,"class","p-fix w-100 h-100 svelte-s7kz7x"),l(s,"id","popup")},m(t,u){T(t,s,u),C(s,e),V(e,i[1]),r||(o=A(e,"input",i[9]),r=!0)},p(t,u){u&2&&V(e,t[1])},d(t){t&&h(s),r=!1,o()}}}function he(i){let s,e,r="TogglePrint",o,t,u="Print",v,m,g,p,x,z,f,I,k,a,_,b;function N(n){i[7](n)}let P={lang:ae({base:ce,codeLanguages:de,completeHTMLTags:!0}),theme:ie,basic:!0,styles:re,lineWrapping:!0,placeholder:"Type some markdown here..."};i[0]!==void 0&&(P.value=i[0]),p=new le({props:P}),q.push(()=>X(p,"value",N)),p.$on("change",i[3]);let c=i[1].length&&M(i);return{c(){s=w("div"),e=w("div"),e.textContent=r,o=D(),t=w("div"),t.textContent=u,v=D(),m=w("main"),g=w("div"),G(p.$$.fragment),z=D(),f=w("iframe"),I=D(),c&&c.c(),k=L(),this.h()},l(n){s=y(n,"DIV",{class:!0,id:!0});var d=j(s);e=y(d,"DIV",{class:!0,"data-svelte-h":!0}),R(e)!=="svelte-cksdy8"&&(e.textContent=r),o=S(d),t=y(d,"DIV",{class:!0,"data-svelte-h":!0}),R(t)!=="svelte-1nctn6c"&&(t.textContent=u),d.forEach(h),v=S(n),m=y(n,"MAIN",{class:!0});var E=j(m);g=y(E,"DIV",{class:!0});var $=j(g);J(p.$$.fragment,$),$.forEach(h),z=S(E),f=y(E,"IFRAME",{id:!0,frameborder:!0,title:!0,style:!0,class:!0}),j(f).forEach(h),E.forEach(h),I=S(n),c&&c.l(n),k=L(),this.h()},h(){l(e,"class","rx10 ptr svelte-s7kz7x"),l(t,"class","rx10 ptr svelte-s7kz7x"),l(s,"class","f j-ar p-fix w-50 svelte-s7kz7x"),l(s,"id","funcs"),l(g,"class","editor svelte-s7kz7x"),l(f,"id","mfWHAT"),l(f,"frameborder","0"),l(f,"title","Editor Output"),B(f,"background","#888"),l(f,"class","svelte-s7kz7x"),l(m,"class","f fw svelte-s7kz7x")},m(n,d){T(n,s,d),C(s,e),C(s,o),C(s,t),T(n,v,d),T(n,m,d),C(m,g),Q(p,g,null),C(m,z),C(m,f),i[8](f),T(n,I,d),c&&c.m(n,d),T(n,k,d),a=!0,_||(b=[A(fe,"keyup",i[6]),A(e,"click",i[4]),A(t,"click",i[5])],_=!0)},p(n,[d]){const E={};!x&&d&1&&(x=!0,E.value=n[0],F(()=>x=!1)),p.$set(E),n[1].length?c?c.p(n,d):(c=M(n),c.c(),c.m(k.parentNode,k)):c&&(c.d(1),c=null)},i(n){a||(Z(p.$$.fragment,n),a=!0)},o(n){ee(p.$$.fragment,n),a=!1},d(n){n&&(h(s),h(v),h(m),h(I),h(k)),te(p),i[8](null),c&&c.d(n),_=!1,H(b)}}}function ve(i,s,e){let r="",o="",t,u,v;const m=(a,_=!0)=>{const{html:b}=ue(a);_&&localStorage.setItem("cquicc-present",a),v.open(),v.write(b),v.close()},g=()=>{const a=r;if(u===a)return 0;u=a,m(a)};U(async()=>{v||(v=t.contentWindow.document);const a=new URLSearchParams(location.search).get("demo"),_=localStorage.getItem("cquicc-present");if(_&&!a)m(_),e(0,r=_);else{const b=(await O(()=>import("../chunks/basic.1b656fae.js"),[],import.meta.url)).default;m(b,!1),e(0,r=b)}document.title+=(-new Date).toString(36)});const p=()=>{const a=/print-pdf/g.test(location.search)?location.href.replace(/\?print-pdf/g,""):location.href+"?print-pdf";window.location.href=a},x=()=>{/print-pdf/g.test(location.search)&&window.frames[0].print()},z=a=>{a.key==="p"&&a.ctrlKey&&p()};function f(a){r=a,e(0,r)}function I(a){q[a?"unshift":"push"](()=>{t=a,e(2,t)})}function k(){o=this.value,e(1,o)}return[r,o,t,g,p,x,z,f,I,k]}class ye extends Y{constructor(s){super(),K(this,s,ve,he,W,{})}}export{ye as component};
