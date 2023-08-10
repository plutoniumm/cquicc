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

let ws = null;
function connectWS ( attempt, then, cb = console.log ) {
  const host = new URL( window.location.href ).host;
  ws = new WebSocket( `ws://${ host }/ws` );
  ws.onopen = function () {
    attempt = 0;
    let data = typeof then == 'function' ? then() : then;

    ws.send( JSON.stringify( { type: 'connect', data } ) );
  };

  ws.onmessage = function ( e ) {
    let data;
    try {
      data = JSON.parse( e.data );
    } catch ( err ) {
      console.log( "Parse Error" );
      data = e.data;
    }
    cb( data );
  };

  ws.onclose = function ( e ) {
    console.log( 'Socket closed. Reconnecting for attempt:', attempt );

    attempt += 1;
    if ( attempt > WS_MAX_RECONNECT_ATTEMPTS ) {
      ws = null;
      return console.log( 'Max retries reached' );
    } else {
      // start from 500ms and increment by 2x each attempt
      let backoff = Math.pow( 2, attempt - 2 ) * 1000; // 1, 2, 4s
      backoff += backoff * 0.5 * Math.random(); // 50% jitter
      backoff = backoff | 0; // round to int

      console.log( "Waiting", backoff / 1000, "s" );
      setTimeout( () =>
        connectWS( attempt, then, cb ),
        backoff
      );
    }
  };

  ws.onerror = function ( err ) {
    console.error( 'Socket encountered error: ', err.message, 'Closing socket' );
    ws.close();
  };
};

function then () {
  return {
    run: "connected",
    data: {
      test: "check",
    }
  };
};
function cb ( data ) {
  console.log( "GOT: ", data );
};

connectWS( 0, then, cb );

function closeWS () {
  if ( ws ) {
    ws.close();
    ws = null;
  }
}