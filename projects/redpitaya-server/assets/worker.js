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

// *************
// MAIN FUNCTIONS
// *************
/**
 @returns {Promise<string[]>}
*/
const getData = async () => {
  let data = [];
  data = await Promise.all( [
    p( '/data/spingrid.csv' ), // grid
    p( '/data/convergence.csv' ) // loss
  ] ).catch( e => {
    console.log( e );
    data = [];
  } );

  let loss, grid;
  try {
    grid = getValues( data[ 0 ] );
  } catch ( e ) {
    console.log( data[ 0 ] );
    grid = [];
  }
  console.log( data[ 1 ] );
  try {
    loss = getValues( data[ 1 ] );
  } catch ( e ) {
    console.log( data[ 1 ] );
    loss = [];
  }
  return [ grid, loss ];
};

async function main () {
  const [ data, loss ] = await getData();

  self.postMessage( JSON.stringify( {
    data, loss: loss.map(
      ( [ x, y ] ) => ( { x, y } )
    )
  } ) );
};
self.onmessage = () => main();