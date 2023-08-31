import yaml from "js-yaml";
import { marked } from "marked";
import template from "./render.html?raw"

const mcf = { mangle: false, headerIds: false };
export const render = ( text ) => {
  text = text.replaceAll( "===", "\n</section><section>\n" )

  const [ , meta, ...rest ] = text.split( "---" );
  const m = yaml.load( meta.trim(), { json: true } );

  let html = "<section>\n" +
    marked( rest.join( "---" ), mcf ) +
    "\n</section>";

  console.log( html );
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