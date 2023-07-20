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