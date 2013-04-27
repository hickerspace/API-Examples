var interval = null;

function load_data(initial) {
	var url = "http://hickerspace.org/api/";
	// load initial data via normal api request, later via long polling
	url += initial ? 'ampel/' : 'poll/ampel/';
	
	// request data (with long timeout), display it and start 
	// a new polling (also if last request timed out)
	$.ajax({ url: url,
			success: function(data) {
						display_data(data);
						},
			complete: function() {
						load_data();
						},
			timeout: 60000,
			dataType: "json"
	});
	return true;
}

function display_data(data) {
	if (data) {
		if (data.mode != 'random') {
			// display data the normal way
			if (interval) interval = window.clearInterval(interval);
			setColors(data.red, data.yellow, data.green);
		} else {
			// random mode: fake some random switches
			// beware: there's no light status for random mode
			// (due to high load)
			interval = window.setInterval(function() {
				var red = (Math.floor(Math.random() * 2) == 0);
				var yellow = (Math.floor(Math.random() * 2) == 0);
				var green = (Math.floor(Math.random() * 2) == 0);
				setColors(red, yellow, green);
			}, 1000);
		}
		// set the switching mode
		$('span#mode').html('Mode: ' + data.mode);
	}
}

// turn lights on/off
function setColors(red, yellow, green) {
	// first color value is 'on', second is 'off' (darker color)
	var red = red ? 'red' : '#4D0000';
	var yellow = yellow ? 'yellow' : '#4D4D00';
	var green = green ? 'green' : '#003300';

	// set the css
	$('span#red').css('background-color', red);
	$('span#yellow').css('background-color', yellow);
	$('span#green').css('background-color', green);
}

$(document).ready(function() {
	// fetch initial data and start the whole polling thing
	load_data(true);
});
