function load_data(initial) {
	var url = (document.location.protocol == 'https:' 
		? 'https' : 'http') + '://hickerspace.org/api/mate-o-meter/';
	$.ajax({ url: url,
		success: function(data) { display_data(data); },
		error: function() { display_error() },
		dataType: "json"
	});
}

function display_data(data) {
	if(typeof data.bottles != 'undefined') {
		$('.fortschritt').css("background", "url('img/liquid.png') no-repeat bottom center")
			.css("top", "auto").html("");

		var summary;
		if (data.bottles == 1) {
			summary = "Es ist noch 1 Flasche volle in unserer Kiste.";
		} else if (data.bottles == 0) {
			summary = "Es sind leider keine vollen Flaschen mehr in unserer Kiste.";
		} else {
			summary = "Es sind noch " + data.bottles + " volle Flaschen in unserer Kiste.";
		}
		$('#bottlesleft').html(summary);
		$('#progresscontainer').prop('title', summary);

		var percentage = Math.round((data.bottles / 20) * 100);
		$('div.fortschritt').css('height', percentage + "%");
		
		// create a new javascript Date object based on the timestamp
		// multiplied by 1000 so that the argument is in milliseconds, not seconds
		var updateDate = new Date(data.lastUpdate*1000);
		var lastUpdate;
		if (updateDate.toDateString() == new Date().toDateString()) {
			lastUpdate = "heute";
		} else {
			var day = updateDate.getDate();
			var month = updateDate.getMonth() + 1;

			if (day < 10) day = "0" + day;
			if (month < 10) month = "0" + month;

			lastUpdate = "am " + day + "." + month + "." + updateDate.getFullYear();
		}
		var minutes = updateDate.getMinutes();
		if (minutes < 10) minutes = "0" + minutes;

		lastUpdate = "Letzte Änderung " + lastUpdate + " um " + updateDate.getHours() + ":" 
			+ minutes + " Uhr.<br />";

		$('#copyright').prepend(lastUpdate);
	} else {
		display_error();
	}
}

function display_error() {
	$('#bottlesleft').html("<span style=\"color:red;\">API-Fehler:</span> Bitte später noch&shy;mals versuchen.");
}

$(document).ready(function() {
	// fetch initial data
	load_data(true);

	// hide mobile url bar
	if (/mobile/i.test(navigator.userAgent)) {
			  window.scrollTo(0, 1);
	}
});
