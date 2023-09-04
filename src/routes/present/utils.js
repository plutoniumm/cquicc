import yaml from "js-yaml";
import { marked } from "marked";
import template from "./render.html?raw"

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

export const prerender = ( dom ) => {
  dom.querySelectorAll( ".killCSS" ).forEach( ( e ) => e.remove() );

  const prefix =
    `<head><scr` +
    `ipt src="/reveal.js"></scr` +
    `ipt>
<link rel="stylesheet" href="https://manav.ch/atomic.css">
<link rel="stylesheet" href="/css/reveal.css">
<link rel="stylesheet" href="/css/revealmod.css"></head><body  xmlns="http://www.w3.org/2000/svg">`;

  return prefix + dom.innerHTML + "</body>";
};