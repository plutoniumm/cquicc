var $ = ( selector ) => document.querySelector( selector )
var $$ = ( selector ) => [ ...document.querySelectorAll( selector ) ]
var loop = ( fn ) => setTimeout( fn, 1000 );

var setScroll = () => localStorage.setItem( 'scrollPosition', window.scrollY );
var getScroll = () => {
  const p = localStorage.getItem( 'scrollPosition' )
  if ( p ) window.scrollTo( 0, parseInt( p ) );
};

window.addEventListener( 'scroll', setScroll );
window.addEventListener( 'load', getScroll );