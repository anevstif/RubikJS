class Rubic {
	constructor(taskCommand, size) {
		this.keyStatus = "none";
		this.axisRotation = "";
		this.segmentRotation = 0;
		this.directionRotation = 0;
		this.size = parseInt(size) || 3;
		this.geom = new RubicGeometry(this.size);
		this.world = new World(this.size, this.geom.getGeom());
		this.speed = 1;
		this.command = (taskCommand) ? taskCommand.split(' ') : [];
	}
}

function animate() 
{
	let deltasec = r.world.update() * r.speed;
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
	var backSide = false;
	switch(item[0]) {
	case "U":
		r.axisRotation = "y";
		r.segmentRotation = r.size - 1;
		break;
	case "D":
		r.axisRotation = "y";
		r.segmentRotation = 0;
		backSide = true;
		break;
	case "R":
		r.axisRotation = "x";
		r.segmentRotation = r.size - 1;
		break;
	case "L":
		r.axisRotation = "x";
		r.segmentRotation = 0;
		backSide = true;
		break;
	case "F":
		r.axisRotation = "z";
		r.segmentRotation = r.size - 1;
		break;
	case "B":
		r.axisRotation = "z";
		r.segmentRotation = 0;
		backSide = true;
		break;
	}

	let v = String(item.substring(1));
	switch(v) {
	case " ":
		if (backSide) {
			r.directionRotation = 1;
		} else {
			r.directionRotation = -1;
		} break;
	case "'":
	case "' ":
	case "'":
	case "%27":
	case "%27 ":
		if (backSide) {
			r.directionRotation = -1;
		} else {
			r.directionRotation = 1;
		} break;
	case "2 ":
		if (backSide) {
			r.directionRotation = 2;
		} else {
			r.directionRotation = -2;
		} break;
	}
	r.geom.groupToPivot(r.axisRotation, r.segmentRotation);
	r.keyStatus = "direction";
}

function btnClick() {
	taskCommand = document.getElementById("task").value;
	r.command = (taskCommand) ? taskCommand.split(' ') : [];
	r.geom = new RubicGeometry(r.size);
	r.world.remup(r.size, r.geom.getGeom());
	r.keyStatus = "start";
}

function spdInp() {
	r.speed = document.getElementById("speed").value;
}

function slvBtn() {
$(document).ready(function (){
    $.ajax({
      url: '/ajax',
      type: "post",
      data: "Lorem ipsum dolor sit amet, ",
      dataType: 'html',
      beforeSend: function() {
        console.info("loading...");
      },
      success: afterSend
    });
  });
}
function afterSend(result) {
    console.info("result:" + result);
};

taskCommand = ""
elem = document.getElementById("task");
if (elem != null) {
	taskCommand = elem.innerHTML;
}
var r = new Rubic(taskCommand);
animate();