import App from './App.svelte';
export default new App( { target: document.body } );

setTimeout( () => {
  let dt = ( +new Date() / 1000 ) % 100_000;

  document.title = document.title + ( dt | 0 );
}, 50 );