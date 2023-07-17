// preventdefault
// post to /rce with text as body
const form = document.querySelector( "#rce" );
function runRCE ( e ) {
  e.preventDefault();

  console.log( e );
  const form = document.querySelector( 'form' );
  const data = new FormData( form );

  console.log( data, form );

  fetch( '/rce', {
    method: 'POST',
    body: data
  } )
    .then( res => res.text() )
    .then( res => {
      console.log( res );
      alert( res );
    } )
    .catch( err => {
      console.log( err );
      alert( err );
    } );
};
form.addEventListener( 'submit', runRCE );