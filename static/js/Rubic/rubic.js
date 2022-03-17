class Rubic {
	constructor(size) {
		this.size = parseInt(size) || 3;
		this.taskCommands = [];
		this.solverCommands = [];
		this.currentTaskIndex = 0;
		this.currentSolverIndex = 0;
		this.updateTaskSolver()
		this.keyStatus = "none";
		this.axisRotation = "";
		this.segmentRotation = 0;
		this.directionRotation = 0;
		this.geom = new RubicGeometry(this.size);
		this.world = new World(this.size, this.geom.getGeom());
		this.speed = 1;
	}

	updateTaskSolver() {
		let elem  = getTaskSolver();
		this.taskCommands = elem.task;
		this.solverCommands = elem.solver;
		this.currentTaskIndex = 0;
		this.currentSolverIndex = 0;
	}

	setToMove() {
		if (this.keyStatus == "startTask") {
			this.setToMoveCommand(this.taskCommands[this.currentTaskIndex])
			this.keyStatus = "startRotate";
			this.currentTaskIndex += 1;
			if (this.currentTaskIndex > this.taskCommands.length){
				this.keyStatus = "endTask";
				this.currentTaskIndex = 0;
			}
		}
		if (this.keyStatus == "startSolver") {
			this.setToMoveCommand(this.solverCommands[this.currentSolverIndex])
			this.keyStatus = "solverRotate";
			this.currentSolverIndex += 1;
			if (this.currentSolverIndex > this.solverCommands.length){
				this.keyStatus = "none";
				this.currentSolverIndex = 0;
			}
		}
	}

	setToMoveCommand(command) {
		let item = command + " ";
		var backSide = false;
		switch(item[0]) {
			case "U":
				this.axisRotation = "y";
				this.segmentRotation = this.size - 1;
				break;
			case "D":
				this.axisRotation = "y";
				this.segmentRotation = 0;
				backSide = true;
				break;
			case "R":
				this.axisRotation = "x";
				this.segmentRotation = this.size - 1;
				break;
			case "L":
				this.axisRotation = "x";
				this.segmentRotation = 0;
				backSide = true;
				break;
			case "F":
				this.axisRotation = "z";
				this.segmentRotation = this.size - 1;
				break;
			case "B":
				this.axisRotation = "z";
				this.segmentRotation = 0;
				backSide = true;
				break;
		}

		let v = String(item.substring(1));
		switch(v) {
			case " ":
				if (backSide) {
					this.directionRotation = 1;
				} else {
					this.directionRotation = -1;
				} break;
			case "'":
			case "' ":
			case "'":
			case "%27":
			case "%27 ":
				if (backSide) {
					this.directionRotation = -1;
				} else {
					this.directionRotation = 1;
				} break;
			case "2 ":
				if (backSide) {
					this.directionRotation = 2;
				} else {
					this.directionRotation = -2;
				} break;
		}
		this.geom.groupToPivot(this.axisRotation, this.segmentRotation);
	}

	update() {
		let deltasec = this.world.update() * this.speed;
		if ((this.keyStatus == "startRotate") || (this.keyStatus == "solverRotate")) {
			if (this.geom.rotateGeom(
				this.axisRotation,
				this.segmentRotation,
				this.directionRotation,
				deltasec)
			) {
				//function() {
				if (this.keyStatus == "startRotate") {
					this.keyStatus = "startTask";
				} else if (this.keyStatus == "solverRotate") {
					this.keyStatus = "startSolver";
				}
			}
			//});
		} else if ((this.keyStatus == "startTask") || (this.keyStatus == "startSolver")) {
			this.setToMove();
		}
		this.world.render();
	}
}
