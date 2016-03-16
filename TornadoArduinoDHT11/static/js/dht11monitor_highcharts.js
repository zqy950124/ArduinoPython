


ws = new WebSocket("ws://" + window.location.host + "/websocket");

ws.onmessage = function(evt) {
	var msg = evt.data;
	console.log(msg);
	obj = JSON.parse(msg);
	var temperature = document.getElementById("temperatureLBL");
	temperature.innerText='temperature:'+obj.d0;
	
	var humidity = document.getElementById("humidityLBL");
	humidity.innerText='humidity:'+obj.d1;
	
	var heatindex = document.getElementById("heatindexLBL");
	heatindex.innerText='heatindex:'+obj.d2;
	

}

