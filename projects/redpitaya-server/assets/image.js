const canvas = $( "#pCanvas" );
const ctx = canvas.getContext( "2d" );

const lossplot = $( "#lossplot" );

/**
  @param {number[][]} values
  @returns {string}
*/
function generateHeat ( values ) {
  // chessboard from nxn values on canvas
  const n = Math.sqrt( values.length );
  const w = canvas.width / n; // width of each square
  const h = w;
  console.log( values );

  // draw chessboard
  for ( let i = 0;i < values.length;i++ ) {
    const x = i % n;
    const y = Math.floor( i / n );
    const row = values[ i ];

    ctx.fillStyle = row[ 2 ] ? "red" : "blue";
    ctx.fillRect( x * w, y * h, w, h );
  }
};

function generateLoss ( values ) {
  // data is of form [x1,y1],[x2,y2],...
  const data = values;

  // Create an SVG element
  const svg = document.createElement( "svg" );
  svg.setAttribute( "width", "500" );
  svg.setAttribute( "height", "500" );
  const path = document.createElement( "path" );

  // Generate the d attribute for the path by converting data points to a smooth line
  const d = "M" + data.map( ( point, index ) => {
    if ( index === 0 ) {
      return `${ point[ 0 ] },${ point[ 1 ] }`;
    } else {
      const prevPoint = data[ index - 1 ];
      const dx = ( point[ 0 ] - prevPoint[ 0 ] ) / 2;
      return `C ${ prevPoint[ 0 ] + dx },${ prevPoint[ 1 ] } ${ point[ 0 ] - dx },${ point[ 1 ] } ${ point[ 0 ] },${ point[ 1 ] }`;
    }
  } ).join( " " );

  // Set the d attribute of the path
  path.setAttribute( "d", d );
  path.setAttribute( "fill", "none" );
  path.setAttribute( "stroke", "blue" );
  path.setAttribute( "stroke-width", "2" );

  svg.appendChild( path );
  document.body.appendChild( svg );
}