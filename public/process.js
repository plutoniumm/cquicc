const $ = ( selector ) => document.querySelector( selector )
const $$ = ( selector ) => [ ...document.querySelectorAll( selector ) ]
const loop = ( fn ) => setTimeout( fn, 1000 );