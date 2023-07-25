const base = new URL( window.location.href )

async function check_scpi () {
  const host = "/scpi";

  const response = await fetch( host, { method: 'HEAD' } );

  return response.status === 200;
};

check_scpi().then( ( scpi ) => {
  console.log( "SCPI:", scpi );
} );

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
  }, 3000 );
};

document.body.addEventListener( "htmx:afterRequest", function ( e ) {
  response = e.detail;
  if ( response.error ) {
    createErrorNode( "Unknown Error at " + response.pathInfo.requestPath )
  };
} );