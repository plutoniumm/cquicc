import{_ as F}from"../chunks/preload-helper.a4192956.js";import{s as X,p as U,f as k,a as I,e as q,g as b,h as S,A as V,c as j,d as v,j as m,k as M,i as D,x as g,B as A,C as Y,D as W,o as G,E as B}from"../chunks/scheduler.3fe22ecb.js";import{S as K,i as J,f as Q,b as Z,d as ee,m as te,a as ne,t as se,e as ae}from"../chunks/index.a14d807c.js";import{j as le,c as re,m as ie,d as oe,a as ce,C as de,g as me,b as fe,l as ue}from"../chunks/utils.715bece7.js";const pe=`<!DOCTYPE html>
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

</html>`,he={mangle:!1,headerIds:!1},ve=r=>{const[,e,...t]=r.split("---"),o=le.load(e.trim(),{json:!0});let n=t.join("---").split("===").map(l=>re(l,he)).join("</section><section>");n=pe.replace("&head;","").replace("&body;",`<section>${n}</section>`);for(let l in o)n=n.replace(`&${l};`,o[l]);return{meta:o,html:n}};const{window:_e}=me;function H(r){let e,t,o,n,l="X",w,u;return{c(){e=k("div"),t=k("textarea"),o=I(),n=k("button"),n.textContent=l,this.h()},l(i){e=b(i,"DIV",{class:!0,id:!0});var f=S(e);t=b(f,"TEXTAREA",{name:!0,class:!0}),S(t).forEach(v),o=j(f),n=b(f,"BUTTON",{class:!0,style:!0,"data-svelte-h":!0}),V(n)!=="svelte-1l4u4xv"&&(n.textContent=l),f.forEach(v),this.h()},h(){m(t,"name","code"),m(t,"class","rpm-10 flow-y-s svelte-flfytx"),m(n,"class","d-b rx20 mx-a ptr"),M(n,"color","#fff"),M(n,"background","#f00"),M(n,"width","50px"),m(e,"class","p-fix blur tc svelte-flfytx"),m(e,"id","popup")},m(i,f){D(i,e,f),g(e,t),B(t,r[1]),g(e,o),g(e,n),w||(u=[A(t,"input",r[10]),A(n,"click",r[11])],w=!0)},p(i,f){f&2&&B(t,i[1])},d(i){i&&v(e),w=!1,W(u)}}}function ge(r){let e,t,o="TogglePrint",n,l,w="Print",u,i,f="GetCode",E,_,x,p,L,P,h,R,a,y,C,N;function z(s){r[8](s)}let O={lang:ie({base:fe,codeLanguages:ue,completeHTMLTags:!0}),theme:oe,basic:!0,styles:ce,lineWrapping:!0,placeholder:"Type some markdown here..."};r[0]!==void 0&&(O.value=r[0]),p=new de({props:O}),U.push(()=>Q(p,"value",z)),p.$on("change",r[3]);let c=r[1].length&&H(r);return{c(){e=k("div"),t=k("div"),t.textContent=o,n=I(),l=k("div"),l.textContent=w,u=I(),i=k("div"),i.textContent=f,E=I(),_=k("main"),x=k("div"),Z(p.$$.fragment),P=I(),h=k("iframe"),R=I(),c&&c.c(),a=q(),this.h()},l(s){e=b(s,"DIV",{class:!0,id:!0});var d=S(e);t=b(d,"DIV",{class:!0,"data-svelte-h":!0}),V(t)!=="svelte-cksdy8"&&(t.textContent=o),n=j(d),l=b(d,"DIV",{class:!0,"data-svelte-h":!0}),V(l)!=="svelte-1nctn6c"&&(l.textContent=w),u=j(d),i=b(d,"DIV",{class:!0,"data-svelte-h":!0}),V(i)!=="svelte-1hb0lwa"&&(i.textContent=f),d.forEach(v),E=j(s),_=b(s,"MAIN",{class:!0});var T=S(_);x=b(T,"DIV",{class:!0});var $=S(x);ee(p.$$.fragment,$),$.forEach(v),P=j(T),h=b(T,"IFRAME",{id:!0,frameborder:!0,title:!0,style:!0,class:!0}),S(h).forEach(v),T.forEach(v),R=j(s),c&&c.l(s),a=q(),this.h()},h(){m(t,"class","rx10 ptr svelte-flfytx"),m(l,"class","rx10 ptr svelte-flfytx"),m(i,"class","rx10 ptr svelte-flfytx"),m(e,"class","f j-ar p-fix w-50 svelte-flfytx"),m(e,"id","funcs"),m(x,"class","editor svelte-flfytx"),m(h,"id","mfWHAT"),m(h,"frameborder","0"),m(h,"title","Editor Output"),M(h,"background","#888"),m(h,"class","svelte-flfytx"),m(_,"class","f fw svelte-flfytx")},m(s,d){D(s,e,d),g(e,t),g(e,n),g(e,l),g(e,u),g(e,i),D(s,E,d),D(s,_,d),g(_,x),te(p,x,null),g(_,P),g(_,h),r[9](h),D(s,R,d),c&&c.m(s,d),D(s,a,d),y=!0,C||(N=[A(_e,"keyup",r[6]),A(t,"click",r[4]),A(l,"click",r[5]),A(i,"click",r[7])],C=!0)},p(s,[d]){const T={};!L&&d&1&&(L=!0,T.value=s[0],Y(()=>L=!1)),p.$set(T),s[1].length?c?c.p(s,d):(c=H(s),c.c(),c.m(a.parentNode,a)):c&&(c.d(1),c=null)},i(s){y||(ne(p.$$.fragment,s),y=!0)},o(s){se(p.$$.fragment,s),y=!1},d(s){s&&(v(e),v(E),v(_),v(R),v(a)),ae(p),r[9](null),c&&c.d(s),C=!1,W(N)}}}function ye(r,e,t){let o="",n="",l,w,u;const i=(a,y=!0)=>{const{html:C}=ve(a);y&&localStorage.setItem("cquicc-present",a),u.open(),u.write(C),u.close()},f=()=>{const a=o;if(w===a)return 0;w=a,i(a)};G(async()=>{u||(u=l.contentWindow.document);const a=new URLSearchParams(location.search).get("demo"),y=localStorage.getItem("cquicc-present");if(y&&!a)i(y),t(0,o=y);else{const C=(await F(()=>import("../chunks/basic.1b656fae.js"),[],import.meta.url)).default;i(C,!1),t(0,o=C)}document.title+=(-new Date).toString(36)});const E=()=>{const a=/print-pdf/g.test(location.search)?location.href.replace(/\?print-pdf/g,""):location.href+"?print-pdf";window.location.href=a},_=()=>{/print-pdf/g.test(location.search)&&window.frames[0].print()},x=a=>{a.key==="p"&&a.ctrlKey&&E()},p=()=>t(1,n=window.frames[0].document.body.innerHTML);function L(a){o=a,t(0,o)}function P(a){U[a?"unshift":"push"](()=>{l=a,t(2,l)})}function h(){n=this.value,t(1,n)}return[o,n,l,f,E,_,x,p,L,P,h,()=>t(1,n="")]}class Ce extends K{constructor(e){super(),J(this,e,ye,ge,X,{})}}export{Ce as component};
