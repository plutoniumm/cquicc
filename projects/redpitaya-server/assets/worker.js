/**
 @param {string} file
 @returns {Promise<string>}
*/
const p = async ( file ) => {
  let err = null;
  let res = await fetch( file )
    .catch( e => err = e );
  if ( res.ok || !err ) {
    const t = await res.text();
    if ( !t ) {
      return "";
    } else {
      return t.replace( '-e', '' )
    }
  } else {
    return "";
  }
};
/**
 * @param {string} str
 * @returns {number[][]}
*/
const getValues = ( str ) => str.trim().split( "\n" )
  .map( r => r.split( "," ).map( v => +( v.trim() ) ) );
const extractValue = ( str ) => {
  try {
    str = getValues( str );
    return str;
  } catch ( e ) {
    console.log( "Err:", str );
    return [];
  }
}

// *************
// MAIN FUNCTIONS
// *************
/**
 @returns {Promise<string[]>}
*/
const getData = async () => {
  const rand = ( ( Math.random() * 10e10 ) | 0 ).toString( 36 );
  // for cache busting
  let data = [];
  data = await Promise.all( [
    p( '/data/spingrid.csv?' + rand ), // grid
    p( '/data/convergence.csv?' + rand ) // loss
  ] );

  if ( !data?.length ) return [];
  data = data.map( extractValue );
  data[ 1 ] = data[ 1 ]
    .map( ( [ x, y ] ) => ( { x, y } ) );

  return JSON.stringify( data );
};

self.onmessage = async () => {
  const data = await getData();
  self.postMessage( data );
}