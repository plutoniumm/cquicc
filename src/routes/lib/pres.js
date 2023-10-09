import yaml from "js-yaml";
import { marked } from "marked";
import template from "../present.html?raw"

const mcf = { mangle: false, headerIds: false };
export const render = ( text ) => {
  const [ , meta, ...rest ] = text.split( "---" );
  const m = yaml.load( meta?.trim(), { json: true } );

  let html = rest
    .join( "---" )
    .split( "===" )
    .map( section => marked( section, mcf ) )
    .join( "</section><section data-auto-animate>" );

  html = template
    .replace( "&head;", "" )
    .replace( "&body;", `<section data-auto-animate>${ html }</section>` );

  for ( let key in m )
    html = html.replace( `&${ key };`, m[ key ] );

  return {
    meta: m,
    html,
  }
};