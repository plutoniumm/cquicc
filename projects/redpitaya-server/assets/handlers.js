const base = new URL( window.location.href )

document.querySelectorAll( '[tx]' ).forEach( el => {
  el.style.color = el.getAttribute( 'tx' );
} );
document.querySelectorAll( '[bg]' ).forEach( el => {
  el.style.backgroundColor = el.getAttribute( 'bg' );
} );
document.querySelectorAll( '[flex]' ).forEach( el => {
  el.style.flex = el.getAttribute( 'flex' ) || 1;
} );

const errorHolder = document.querySelector( '#error-holder' );
const errorNodes = [];
const createErrorNode = ( msg ) => {
  const errorNode = document.createElement( 'div' );
  errorNode.classList.add( 'error' );
  errorNode.innerText = msg;
  errorHolder.appendChild( errorNode );
  errorNodes.push( errorNode );

  setTimeout( () => {
    errorNode.remove();
    errorNodes.splice( errorNodes.indexOf( errorNode ), 1 );
  }, 6e3 );
};

document.body.addEventListener( "htmx:afterRequest", function ( e ) {
  let error = "Unknown Error";
  let response = e.detail;

  if ( response.error ) {
    if ( response.status == 500 ) {
      error = "Server Error";
    }
    createErrorNode( error + " at " + response.pathInfo.requestPath )
  };
} );