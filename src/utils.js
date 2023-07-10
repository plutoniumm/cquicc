import typeset from "typeset";
import { marked } from "marked";
import yaml from "js-yaml";
import template from "./render.html?raw"

export const defStyles = {
  "&": {
    fontSize: "18px",
    height: "100%",
    width: "100%",
  },
}

export const render = ( text ) => {
  const [ , meta, ...rest ] = text.split( "---" );

  const m = yaml.load( meta.trim(), { json: true } );
  m.year = new Date( m.date ).getFullYear();
  m.date = new Date( m.date ).toLocaleDateString( 'en-GB' );

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