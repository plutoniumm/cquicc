// *************
// INITIAL DEFS
// *************
/**
 @param {string} file
 @returns {Promise<string>}
*/
const p = ( file ) => fetch( file ).then( r => r.text() );
/**
 * @param {string} str
 * @returns {number[][]}
*/
const getValues = ( str ) => str.trim().split( "\n" )
  .map( r => r.split( "," ).map( v => +( v.trim() ) ) );

/**
 * @param {number} x
 * @param {number} y
 * @param {number} w
 * @param {number} h
 * @param {string} color
 * @returns {string}
*/
const rect = ( x, y, w, h, color = "#000" ) => `<rect x="${ x }" y="${ y }" width="${ w }" height="${ h }" fill="${ color }" />`;

// *************
// MAIN FUNCTIONS
// *************
/**
 @returns {Promise<string[]>}
*/
const getData = async () => {
  const data = await Promise.all( [
    p( '/data/send.txt' ),
    p( '/data/loss.txt' )
  ] );

  return data.map( getValues );
};



async function main () {
  const [ data, loss ] = await getData();

  self.postMessage( JSON.stringify( {
    data, loss: loss.map(
      ( [ x, y ] ) => ( { x, y } )
    )
  } ) );
};

self.onmessage = async function ( e ) {
  const data = await main();
  self.postMessage( data );
};
