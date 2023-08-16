// fetch datafile, fetch loss file
// datafile => grid svg & lossfile => loss plot
/**
 @param {string} file
 @returns {Promise<string>}
*/
const p = ( file ) => fetch( file ).then( r => r.text() );

/**
 @returns {Promise<string[]>}
*/
const getData = async () => {
  const data = await Promise.all( [
    p( '/data/send.txt' ),
    p( '/data/loss.txt' )
  ] );

  return data;
};

/**
  @param {number[][]} values
  @returns {string}
*/
function generateImage ( values ) {
  var image = [];
  const px = 10;
  for ( let i = 0;i < values.length;i++ ) {
    for ( let j = 0;j < values[ 0 ].length;j++ ) {
      image.push(
        rect(
          px * i, px * j, px, px,
          values[ i ][ j ] ? "#000" : "#fff"
        )
      );
    };
  };

  return `<svg width="${ 2 * values.length }" height="${ 2 * values[ 0 ].length }">
    ${ image.join( "" ) }
  </svg>`;
};


async function main () {
  const [ datafile, lossfile ] = await getData();

  self.postMessage( JSON.stringify( {
    data: datafile,
    loss: lossfile
  } ) );
};

self.onmessage = async function ( e ) {
  const data = await main();
  self.postMessage( data );
};
