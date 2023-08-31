import App from './App.svelte';
export default new App( { target: document.body } );

setTimeout( () => (
  document.title += ( -new Date() ).toString( 36 )
), 50 )