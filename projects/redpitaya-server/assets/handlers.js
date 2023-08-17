const base = new URL( window.location.href );
const WS_MAX_RECONNECT_ATTEMPTS = 10;
const ERROR_TIMEOUT = 6e3;

$$( '[tx]' ).forEach( e => setStyle( e, 'color', "tx" ) );
$$( '[bg]' ).forEach( e => setStyle( e, 'backgroundColor', "bg" ) );
$$( '[flex]' ).forEach( e => setStyle( e, 'flex', "flex" ) );

const errorHolder = $( '#error-holder' );
const errorNodes = [];
const createErrorNode = ( msg, type = "error", time = ERROR_TIMEOUT ) => {
  msg = typeof msg == "string" ? msg : msg.message;
  const errorNode = document.createElement( 'div' );
  errorNode.classList.add( type );
  errorNode.innerText = msg;
  errorHolder.appendChild( errorNode );
  errorNodes.push( errorNode );

  setTimeout( () => {
    errorNode.remove();
    errorNodes.splice( errorNodes.indexOf( errorNode ), 1 );
  }, time );
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



let iter = 0;
async function update () {
  work( "start" ).then( d => {
    const { data, loss } = JSON.parse( d );
    const t = [ generateLoss( loss ), generateHeat( data ) ]
  } ).catch( e => {
    createErrorNode( "Connection Error", e.message );
  } );
}

// variable rate
const autoUpdate = () => {
  const Rrate = rate.value || 1;
  setTimeout( () => {
    if ( calling ) {
      console.log( "Updating...", iter++ );
      update();
    };
    autoUpdate( rate );
  }, Rrate * 1000 );
}; autoUpdate();

const BEGIN = () => {
  calling = true;
}
const END = ( reason = "unspecified" ) => {
  console.log( "Ending Reason: ", reason );
  toggle();
  iter = 0;
  fetch( '/kill/child' ).catch( e => console.log( "Killed" ) );
}

createErrorNode( "Loaded Server Handler", "success", 500 )