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

  const metaObj = yaml.load( meta.trim(), { json: true } );

  let html = marked( rest.join( "---" ) );
  html = typeset( html );

  html = template.replace( "&body;", html );

  return {
    meta: metaObj,
    html,
  }
}