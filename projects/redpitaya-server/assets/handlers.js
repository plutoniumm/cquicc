// preventdefault
const form = document.querySelector( "#rce" );
// function runRCE ( e ) {
//   e.preventDefault();
//   const code = document.querySelector( '#rce-code' ).value
//   console.log( code );

//   fetch( '/rce', {
//     method: 'POST',
//     // body: JSON.stringify( code.split( ' ' ) )
//     body: code
//   } )
//     .then( res => res.text() )
//     .then( res => {
//       console.log( res );
//     } )
//     .catch( err => {
//       console.log( err );
//     } );
// };
// form.addEventListener( 'submit', runRCE );