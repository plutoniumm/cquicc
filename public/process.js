var $ = ( selector ) => document.querySelector( selector )
var $$ = ( selector ) => [ ...document.querySelectorAll( selector ) ]
var loop = ( fn ) => setTimeout( fn, 1000 );