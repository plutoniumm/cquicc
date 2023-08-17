const canvas = $( "#pCanvas" );
const ctx = canvas.getContext( "2d" );
const lossPlot = $( "#lCanvas" ).getContext( "2d" );

/**
  @param {number[][]} values
  @returns {string}
*/
function generateHeat ( values ) {
  const n = values.length;
  const w = canvas.width / n; // width of each square
  const h = w;

  // inputs n rows of with n
  for ( let i = 0;i < values.length;i++ ) {
    for ( let j = 0;j < values[ 0 ].length;j++ ) {
      const el = values[ i ][ j ];
      ctx.fillStyle = el ? "#000" : "#fff";
      ctx.fillRect( j * w, i * h, w, h );
    }
  }
};


let chart = null;
async function generateLoss ( values ) {
  if ( chart ) {
    chart.data.datasets[ 0 ].data = values;
    chart.update();
    return 0;
  }
  try {
    chart = new Chart( lossPlot, {
      type: 'scatter',
      data: {
        datasets: [ {
          label: 'Loss',
          data: values,
          backgroundColor: '#f683',
          borderColor: '#f68',
          borderWidth: 1,
        } ]
      },
      options: {
        responsive: true,
      },
    } );
  } catch ( e ) {
    if ( !( values?.length > -1 ) ) {
      createErrorNode( "No Data Recieved. Stopping Plot" );
      END( "No Data Recieved" );
    } else {
      console.log( e );
      createErrorNode( "Unknown Error in LossPlot. Stopping" );
      END( "Unknown Error in LossPlot" );
    }
  };
};