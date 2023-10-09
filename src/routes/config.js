import { render as docRender } from "./doc.js";
import { render as presRender } from "./pres.js";

export const isLocalHost = () => window.location.hostname === "localhost";
const useLocal = ( from = "document" ) => ( isLS, file ) => {
  if ( !file || !isLS ) return (
    await import( "./" + from + ".md?raw" )
  ).default;
  return fetch( `/${ from }/${ file }.md` ).then( r => r.text() );
}

const presentation = {
  useLocal: useLocal( "present" ),
  renderer: "document.html",
  template: "document.md",
  memory: "cquicc-present",
  render: presRender,
};
const documentation = {
  useLocal: useLocal( "document" ),
  renderer: "present.html",
  template: "present.md",
  memory: "cquicc-code",
  render: docRender,
};

export const mode = {
  pres: presentation,
  doc: documentation
}