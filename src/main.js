import App from './App.svelte';
export default new App( { target: document.body } );

setTimeout( () => {
  let dt = ( +new Date() ).toString( 36 );

  document.title = document.title + dt;
}, 50 );