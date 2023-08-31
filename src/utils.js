import markedKatex from "marked-katex-extension";
import { markedHighlight } from "marked-highlight";
import { marked } from "marked";
import hljs from 'highlight.js';
import typeset from "typeset";
import yaml from "js-yaml";

import template from "./render.html?raw"
const mcf = { mangle: false, headerIds: false };

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


export const defStyles = {
  "&": {
    fontSize: "18px",
    height: "100%",
    width: "100%",
  },
}

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

export const render = ( text ) => {
  const pre = "<div class='prep'></div>";
  const post = "<div class='postp'></div>";

  text = text
    .replaceAll( "___", "<hr/>" )
    .replaceAll( "/===", "</div></section>" + post )
    .replaceAll( "===", pre + "<section class='split'><div>" )
    .replaceAll( "+++", "\n\n</div><div>\n\n" )
    .replace( /\[@(\d+)\]/g, ( _, id ) =>
      `<cite><a href="#fn${ id }" id="ref${ id }">[${ id }]</a></cite>`
    );

  const [ , meta, ...rest ] = text.split( "---" );

  const m = yaml.load( meta.trim(), { json: true } );
  if ( !m.date )
    m.date = new Date().toISOString();

  m.vars = JSON.stringify( {
    author: m.author,
    from: m.from,
  } );
  m.year = new Date( m.date ).getFullYear();
  m.date = new Date( m.date ).toLocaleDateString( 'en-GB', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  } );

  let html =
    typeset(
      marked( rest.join( "---" ), mcf )
    );

  html = template
    .replace( "&head;", "" )
    .replace( "&body;", html );

  for ( let key in m )
    html = html.replace( `&${ key };`, m[ key ] );

  return {
    meta: m,
    html,
  }
}