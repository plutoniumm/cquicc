const canvas = $( "#pCanvas" );
const ctx = canvas.getContext( "2d" );

const lossPlot = $( "#lCanvas" ).getContext( "2d" );

/**
  @param {number[][]} values
  @returns {string}
*/
function generateHeat ( values ) {
  const n = Math.sqrt( values.length );
  const w = canvas.width / n; // width of each square
  const h = w;

  for ( let i = 0;i < values.length;i++ ) {
    const [ x, y, val ] = values[ i ];

    ctx.fillStyle = val ? "red" : "blue";
    ctx.fillRect( x * w, y * h, w, h );
  };
};

let chart = null;
function generateLoss ( values ) {
  if ( chart ) chart.destroy();
  try {
    chart = new Chart( lossPlot, {
      type: 'scatter',
      data: {
        datasets: [ {
          label: 'Loss',
          data: values,
          backgroundColor: '#f683',
          borderColor: '#f68',
          borderWidth: 1
        } ]
      },
      options: {
        responsive: true,
        animation: { duration: 0 },
        hover: { animationDuration: 0 },
        responsiveAnimationDuration: 0,
      },
    } );
  } catch ( e ) {
    if ( !( values?.length > 1 ) ) {
      createErrorNode( "No Data Recieved. Stopping Plot" );
      END();
    } else {
      console.log( e );
      createErrorNode( "Unknown Error in LossPlot. Stopping" );
      END();
    }
  };
};