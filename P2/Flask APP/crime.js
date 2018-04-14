  

  var url = "/api/la_county_crime";
  d3.json(url,function(error,response) {
    if (error) return console.warn(error);
    var grand_total = response.pop();
    console.log(grand_total)
  });