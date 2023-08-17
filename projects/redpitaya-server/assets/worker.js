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
    p( '/data/spingrid.csv' ),
    p( '/data/convergence.csv' )
  ] ).catch( e => {
    console.log( e );
    data = [];
  } );

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
self.onmessage = () => main();