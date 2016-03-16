
function switchledon() {
	message="{led:1}";
	ws.send(message);
}

function switchledoff() {
	message="{led:0}";
	ws.send(message);
}