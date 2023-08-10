const plotHolder = $( "#plot-result" );
function diffAndPlot ( data ) {
  data = data.split( "\n" ).slice( 1 );
  const xyz = data.map( d => new Int8Array( d.split( "," ) ) );
  const len = Math.sqrt( xyz.length );

  // init matrix
  const matrix = [];
  for ( let i = 0;i < len;i++ ) {
    const subArr = new Int8Array( len );
    matrix.push( subArr );
  }

  // fill matrix
  for ( let i = 0;i < xyz.length;i++ ) {
    const [ x, y, z ] = xyz[ i ];
    matrix[ x ][ y ] = z;
  }

  const diff = matrixDiff( matrix, makeChessboard( 50 ) );
  const image = generateImage( diff );

  // update image
  plotHolder.innerHTML = image;
};