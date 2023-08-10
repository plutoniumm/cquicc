const form = $( "#startPlot" );



const getData = ( file ) => {
  const reader = new FileReader();
  reader.readAsText( file );
  reader.onload = function () {
    const data = reader.result;
    return data;
  };
}



form.addEventListener( "submit", function ( e ) {
  e.preventDefault();

  const obj = new FormData( form );
  const data = getData( obj.get( "file" ) );
  console.log( data );

  const json = JSON.stringify( {
    run: "start",
    data
  } );

  console.log( json );
  ws.send( json );
  return false;
} );