function buildPlot(): {
  var url = '/api/la_county_crime';
  Plotly.d3.json(url,function(error,crimeData){
    console.log(crimeData);
    var data = [crimeData]

      var layout = {
            title: "testing",
            xaxis: {
                title: "Pet Type"
            },
            yaxis: {
                title: "Number of Pals"
            }
        };

        Plotly.newPlot("crime_graph", data, layout);
    });
}

buildPlot();