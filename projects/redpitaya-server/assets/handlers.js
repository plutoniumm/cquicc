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
    const { data } = JSON.parse( e );

    cb( data );
  };

  ws.onclose = function ( e ) {
    console.log( 'Socket closed. Reconnecting for attempt:', attempt );

    attempt += 1;
    if ( attempt > 5 ) {
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
    run: "start",
    data: {
      id: "test",
      name: "Test",
    }
  };
};
function cb ( data ) {
  console.log( data );
};

connectWS( 0, then, cb );

function closeWS () {
  if ( ws ) {
    ws.close();
    ws = null;
  }
}