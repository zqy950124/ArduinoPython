

var temperatureSeries = new TimeSeries();
var humiditySeries = new TimeSeries();
var heatindexSeries = new TimeSeries();

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
	
	temperatureSeries.append(new Date().getTime(),parseFloat(obj.d0));
	humiditySeries.append(new Date().getTime(), parseFloat(obj.d1));
	HeatIndexSeries.append(new Date().getTime(),  parseFloat(obj.d2));
	
	
}

function createTimeline() {
  var chart = new SmoothieChart();
  chart.addTimeSeries(temperatureSeries);
  chart.addTimeSeries(humiditySeries, { strokeStyle: 'rgba(0, 255, 0, 1)', fillStyle: 'rgba(0, 255, 0, 0.2)', lineWidth: 2 });
  chart.addTimeSeries(heatindexSeries, { strokeStyle: 'rgba(0, 255, 0, 1)', fillStyle: 'rgba(0, 255, 0, 0.2)', lineWidth: 2 });

  chart.streamTo(document.getElementById("chart"), 500);
}

