//this is selecting the variables in the html file
var $tbody = document.querySelector('tbody');
var $stateInput = document.querySelector("#state");
var $searchBtn = document.querySelector("#search");
var $cityInput=document.querySelector("#city");
var $dateInput=document.querySelector('#dateTime');
var $shapeInput=document.querySelector('#shape')

//assigning the object to a variable for easy access
var alien_data=dataSet;

//we need to add an event listener when the user clicks the search button...the 'handleSearchButtonClick' is a function that will be defined later
$searchBtn.addEventListener("click", handleSearchButtonClick);


function fillTable() {
	//there is 'empty' space between the tbody tags, so this is where we choose to render the table with the data.js
	$tbody.innerHTML="";
	//now we are looping through the data.js fill and are adding each i_th element to the fields variable
	for (var i=0;i<alien_data.length;i++){
		//this is storing each i_th element from the data.js file
		var element = alien_data[i];
		// this is grabbing each key within that i_th element (so like, datetime, city, state,etc...)
		var all_fields = Object.keys(element);

		//create a new row in the $tbody 
		var $row = $tbody.insertRow(i);
		for (var j = 0; j< all_fields.length;j++){
			//this is creating column names from the values of the keys in the all_fields variable
			var field=all_fields[j]
			//this will create the cells within the row
			var $cell =$row.insertCell(j);
			//this is filling each cell with the field of each key in the element 
			$cell.innerText = element[field];
		}
	}	

}

function handleSearchButtonClick(){
	//this will adjust the users search so that what ever is inputted it will turn it into lowercase
	var state_search=$stateInput.value.trim().toLowerCase();
	var city_search = $cityInput.value.trim().toLowerCase();
	var date_search= $dateInput.value.trim();
	var shape_search=$shapeInput.value.trim().toLowerCase();

	//filtering the table by the state 
	if (state_search != '') {
		alien_data=dataSet.filter(function(stateFiltered){
		var elementState=stateFiltered.state.toLowerCase();
		return elementState===state_search;
		})
	};



	//filtering the table by the city
	if (city_search != '') {
		alien_data=dataSet.filter(function(cityFiltered){
		var elementCity=cityFiltered.city.toLowerCase();
		return elementCity===city_search;
		})
	};
	

	//filtering the table by date
	if (date_search != '') {
		alien_data=dataSet.filter(function(dateFiltered){
		var elementDate=dateFiltered.datetime.toLowerCase();
		return elementDate===date_search;
		})
	};
	

	if (date_search!=''){
		alien_data=dataSet.filter(function(shapeFiltered){
		var elementShape=shapeFiltered.shape.toLowerCase();
		return elementShape===shape_search;
		})
	};

	fillTable();

	}

fillTable();




