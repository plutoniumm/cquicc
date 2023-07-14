import markedKatex from "marked-katex-extension";
import { markedHighlight } from "marked-highlight";
import { marked } from "marked";
import hljs from 'highlight.js';
import typeset from "typeset";
import yaml from "js-yaml";

import template from "./render.html?raw"

export const defStyles = {
  "&": {
    fontSize: "18px",
    height: "100%",
    width: "100%",
  },
}

const options = {
  katex: {
    throwOnError: false
  },
  hljs: {
    langPrefix: 'hljs language-',
    highlight ( code, lang ) {
      const language = hljs.getLanguage( lang ) ? lang : 'plaintext';
      return hljs.highlight( code, { language } ).value;
    }
  }
}

marked
  .use( markedKatex( options.katex ) )
  .use( markedHighlight( options.hljs ) );

export const render = ( text ) => {
  text = text
    .replaceAll( "/===", "</div></section>" )
    .replaceAll( "===", "<section class='split'><div>" )
    .replaceAll( "+++", "\n\n</div><div>\n\n" );

  const [ , meta, ...rest ] = text.split( "---" );

  const m = yaml.load( meta.trim(), { json: true } );
  if ( !m.date )
    m.date = new Date().toISOString();

  m.year = new Date( m.date ).getFullYear();
  m.date = new Date( m.date ).toLocaleDateString( 'en-GB', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  } );

  let html = marked( rest.join( "---" ) );
  html = typeset( html );

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