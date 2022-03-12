class Rubic {
	constructor(taskCommand, size) {
		this.keyStatus = "start";
		this.axisRotation = "";
		this.segmentRotation = 0;
		this.directionRotation = 0;
		this.size = parseInt(size) || 3;
		this.geom = new RubicGeometry(this.size);
		this.world = new World(this.size, this.geom.getGeom());
		this.command = (taskCommand) ? taskCommand.split(' ') : [];
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
	//console.info(item);
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

	//console.info((item.substring(1)==="%27"));
	let v = String(item.substring(1));
	//console.info("["+(v[3])+"]");
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
		r.directionRotation = -2;
		break;
	default:
		r.directionRotation = 1;
	}
	r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
	r.keyStatus = "direction";
}

taskCommand = ""
elem = document.getElementById("task");
if (elem != null) {
	taskCommand = elem.innerHTML;
}
var r = new Rubic(taskCommand);
animate();