export const prerender = ( dom ) => {
  dom.querySelectorAll( ".killCSS" ).forEach( ( e ) => e.remove() );

  const prefix =
    `<head><scr` +
    `ipt src="/reveal.js"></scr` +
    `ipt>
<link rel="stylesheet" href="https://manav.ch/atomic.css">
<link rel="stylesheet" href="/css/reveal.css">
<link rel="stylesheet" href="/css/revealmod.css"></head><body  xmlns:svg="http://www.w3.org/2000/svg" xmlns:mml="http://www.w3.org/1998/Math/MathML">${ dom.innerHTML }</body>`;

  return prefix;
};

export const isLocalHost = () => window.location.hostname === "localhost";