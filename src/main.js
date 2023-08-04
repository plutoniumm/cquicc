import App from './App.svelte';
export default new App( { target: document.body } );

setTimeout( () => {
  let title = document.title;
  let dt = ( +new Date() / 1000 ) % 100_000;
  dt = dt | 0;

  title += dt;
  document.title = title;

  const url = new URL( window.location.href );
  url.searchParams.set( 't', title );
  window.history.pushState( '', '', url );
}, 50 );