class Rubic {
	constructor(strCommand, size) {
		this.keyStatus = "start";
		this.axisRotation = "";
		this.segmentRotation = 0;
		this.directionRotation = 0;
		this.size = parseInt(size) || 3;
		this.geom = new RubicGeometry(this.size);
		this.world = new World(this.size, this.geom.getGeom());
		this.command = (strCommand) ? strCommand.split('%20') : [];
		document.addEventListener("keyup", keyListener, false);
	}
}

function keyListener(keyDesc) {
	switch (r.keyStatus) {
	case "start":
		let size = parseInt(keyDesc.key) || 0;
		if ((size > 1) && (size < 10)) {
			r.size = size;
			r.geom = new RubicGeometry(size);
			r.world.remup(size, r.geom.getGeom());
		}
		if ((keyDesc.key == "x") || (keyDesc.key == "y") || (keyDesc.key == "z")) {
			r.axisRotation = keyDesc.key;
			r.keyStatus = "axis";
		} else {
			r.keyStatus = "start";
		}
		break;
	case "axis":
		pos = parseInt(keyDesc.key);
		if ((pos != NaN) && (pos >= 0) && (pos < r.size)) {
			r.segmentRotation = pos;
			r.keyStatus = "rotation";
		} else {
			r.keyStatus = "start";
		}
		break;
	case "rotation":
		switch (keyDesc.key) {
		case "+":
			r.directionRotation = 1;
			r.keyStatus = "direction";
			r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
			break;
		case "-":
			r.directionRotation = -1;
			r.keyStatus = "direction";
			r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
			break;
		case "2":
			r.directionRotation = 2;
			r.keyStatus = "direction";
			r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
			break;
		default:
			r.keyStatus = "start";		
		}
	}
}

function animate() 
{
	
	
	let deltasec = r.world.update();
	//console.info(parseFloat(deltasec * 1000.0)+"sec");
	if (r.keyStatus == "direction") {
		r.geom.rotateGeom(r.axisRotation, r.segmentRotation, r.directionRotation, deltasec, function() {
			r.keyStatus = "start";});
	} else if ((r.command.length > 0) && (r.keyStatus == "start")) {
		setToMove();
	}
	r.world.render();
	requestAnimationFrame( animate );
}

function setToMove() {
	let item = r.command.shift().trim() + " ";
	console.info(item);
	switch(item[0]) {
	case "U":
		r.axisRotation = "y";
		r.segmentRotation = r.size - 1;
		break;
	case "D":
		r.axisRotation = "y";
		r.segmentRotation = 0;
		break;
	case "R":
		r.axisRotation = "x";
		r.segmentRotation = r.size - 1;
		break;
	case "L":
		r.axisRotation = "x";
		r.segmentRotation = 0;
		break;
	case "F":
		r.axisRotation = "z";
		r.segmentRotation = r.size - 1;
		break;
	case "B":
		r.axisRotation = "z";
		r.segmentRotation = 0;
		break;
	}

	console.info((item.substring(1)==="%27"));
	let v = String(item.substring(1));
	console.info("["+(v[3])+"]");
	switch(v) {
	case " ":
		r.directionRotation = -1;
		break;
	case "' ":
		r.directionRotation = 1;
		break;
	case "%27 ", "%27":
			console.info("OK");
			r.directionRotation = 1;
			break;
	case "2 ":
		r.directionRotation = 2;
		break;
	default:
		r.directionRotation = 1;
	}
	r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
	r.keyStatus = "direction";
}

function getGETParam(name) {
    var s = window.location.search;
    s = s.match(new RegExp(name + '=([^&=]+)'));
    return s ? s[1] : false;
}

startCommand = getGETParam('start')
var r = new Rubic(startCommand);
animate();