const base = new URL( window.location.href );
const WS_MAX_RECONNECT_ATTEMPTS = 10;
const ERROR_TIMEOUT = 6e3;

$$( '[tx]' ).forEach( e => setStyle( e, 'color', "tx" ) );
$$( '[bg]' ).forEach( e => setStyle( e, 'backgroundColor', "bg" ) );
$$( '[flex]' ).forEach( e => setStyle( e, 'flex', "flex" ) );

const errorHolder = $( '#error-holder' );
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
  }, ERROR_TIMEOUT );
};

document.body.addEventListener( "htmx:afterRequest", function ( e ) {
  let error = "Unknown Error";
  let response = e.detail;

  if ( response.error ) {
    if ( response.status == 500 )
      error = "Server Error";
    createErrorNode( error + " at " + response.pathInfo.requestPath )
  };
} );