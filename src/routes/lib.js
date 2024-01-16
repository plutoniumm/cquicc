import markedKatex from "marked-katex-extension";
import { markedHighlight } from "marked-highlight";
import template from "./present.html?raw"
import { marked } from "marked";
import hljs from 'highlight.js';
import yaml from "js-yaml";

const renderer = {
  // code(string code, string infostring, boolean escaped)
  code ( text, level ) {
    if ( level === "mermaid" ) {
      return `<pre class="mermaid">${ text }</pre>`;
    }
    if ( level === "psd" ) {
      return `<pre class="language-ps">${ text }</pre>`;
    };
    return false;
  }
};

const options = {
  katex: {
    throwOnError: false,
    output: "mathml",
  },
  hljs: {
    langPrefix: 'hljs language-',
    highlight ( code, lang ) {
      if ( lang === "psd" ) {
        const rendered = code
          .split( "\n" )
          .map( ( e, i ) => {
            return `<div class="ps"><m>${ i }:</m>&ensp;${ marked( e, mcf )
              }</div>`;
          } )
          .join( "" );
        return rendered;
      };
      const language = hljs.getLanguage( lang ) ? lang : 'plaintext';
      return hljs.highlight( code, { language } ).value;
    }
  }
}

marked
  .use( markedKatex( options.katex ) )
  .use( markedHighlight( options.hljs ) )
  .use( { renderer } )

const mcf = { mangle: false, headerIds: false };
export const render = ( text ) => {
  const [ , m, ...rest ] = text.split( "---" );
  const meta = yaml.load( m?.trim(), { json: true } );

  let html = rest
    .join( "---" )
    .split( "===" )
    .map( section => marked( section, mcf ) )
    .join( "</section><section data-auto-animate>" );

  html = template
    .replace( "&head;", "" )
    .replace( "&body;", `<section data-auto-animate>${ html }</section>` );

  for ( let key in meta ) {
    html = html.replace( `&${ key };`, meta[ key ] );
  }
  return { meta, html }
};

export const prerender = ( dom ) => {
  dom.querySelectorAll( ".killCSS" ).forEach( ( e ) => e.remove() );

  const prefix =
    `<head><scr` +
    `ipt src="/reveal.js"></scr` +
    `ipt>
<link rel="stylesheet" href="https://manav.ch/atomic.css">
<link rel="stylesheet" href="/assets/reveal.css">
<link rel="stylesheet" href="/assets/revealmod.css"></head><body  xmlns:svg="http://www.w3.org/2000/svg" xmlns:mml="http://www.w3.org/1998/Math/MathML">${ dom.innerHTML }</body>`;

  return prefix;
};

export const isLocalHost = () => window.location.hostname === "localhost";