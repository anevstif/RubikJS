class Rubic {
	constructor(size = 3) {
		this.size = parseInt(size) || 3;
		this.taskCommands = [];
		this.solverCommands = [];
		this.currentTaskIndex = 0;
		this.currentSolverIndex = 0;
		this.keyStatus = "none";
		this.axisRotation = "";
		this.segmentRotation = 0;
		this.directionRotation = 0;
		this.geom = new RubicGeometry(this.size);
		this.world = new World(this.size, this.geom.getGeom());
		this.speed = 1;
	}

	updateTask(commands) {
		this.taskCommands = commands;
		this.currentTaskIndex = 0;
	}

	updateSolver(commands) {
		this.solverCommands = commands;
		this.currentSolverIndex = 0;
	}

	prepareTaskToMove() {
		if (this.currentTaskIndex >= this.taskCommands.length){
			this.keyStatus = "endTask";
			return;
		}
		this.prepareToMoveCommand(this.taskCommands[this.currentTaskIndex])
		this.keyStatus = "taskRotate";
		this.currentTaskIndex += 1;

	}

	prepareSolverToMove() {
		if (this.currentSolverIndex >= this.solverCommands.length){
			this.keyStatus = "none";
			return
		}
		this.prepareToMoveCommand(this.solverCommands[this.currentSolverIndex])
		this.keyStatus = "solverRotate";
		this.currentSolverIndex += 1;
	}


	prepareToMoveCommand(command) {
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
		switch(v[0]) {
			case " ":
			case "\n":
				if (backSide) {
					this.directionRotation = 1;
				} else {
					this.directionRotation = -1;
				} break;
			case "'":
				if (backSide) {
					this.directionRotation = -1;
				} else {
					this.directionRotation = 1;
				} break;
			case "2":
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
		let rotateIsOver;
		switch (this.keyStatus) {
			case "taskRotate":
				rotateIsOver = this.geom.rotateGeom(this.axisRotation, this.segmentRotation, this.directionRotation, deltasec);
				if (rotateIsOver === true) {
					this.keyStatus = "prepareTask";
				}
				break;
			case "solverRotate":
				rotateIsOver = this.geom.rotateGeom(this.axisRotation, this.segmentRotation, this.directionRotation, deltasec);
				if (rotateIsOver === true) {
					this.keyStatus = "prepareSolver";
				}
				break;
			case "prepareTask":
				this.prepareTaskToMove();
				break;
			case "prepareSolver":
				this.prepareSolverToMove();
				break;
		}
		this.world.render();
	}
}
