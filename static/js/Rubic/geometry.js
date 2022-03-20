const BoxType = {Center:0, 
	EdgeTop:1, EdgeLeft:2, EdgeRight:3, EdgeBottom:4,
	CornerTopLeft:5, CornerTopRight:6, CornerBottomLeft:7, CornerBottomRight:8}

const Side = {Top:0, Left:1, Right:2, Front:3, Back:4, Bottom:5}

class RubicBox {
	constructor(x,y,z,delta,boxType,side) {
		var cubeMaterial = createCubeMaterial(boxType, side)
		var cubeGeometry = new THREE.CubeGeometry( 0.95, 0.95, 0.95 );
		this.box = new THREE.Mesh(cubeGeometry, cubeMaterial);
		var turnAngle = THREE.Math.degToRad(90);
		switch(side) {
			case Side.Front:
				this.globalRotation(new THREE.Vector3(1,0,0), turnAngle);
				break;
			case Side.Back:
				this.globalRotation(new THREE.Vector3(1,0,0), -turnAngle);
				break;
			case Side.Left:
				this.globalRotation(new THREE.Vector3(0,0,1), turnAngle);
				break;
			case Side.Right:
				this.globalRotation(new THREE.Vector3(0,0,1), -turnAngle);
				break;
			case Side.Bottom:
				this.globalRotation(new THREE.Vector3(0,0,1), 2 * turnAngle);
		}
		this.box.position.set(x + delta, y + delta, z + delta);
	}
	
	globalRotation(axis, angle) {
		var rotWorldMatrix = new THREE.Matrix4();
		rotWorldMatrix.makeRotationAxis(axis.normalize(), angle);
	
		var currentPos = new THREE.Vector4(this.box.position.x, this.box.position.y, this.box.position.z, 1);
		var newPos = currentPos.applyMatrix4(rotWorldMatrix);
	
		rotWorldMatrix.multiply(this.box.matrix);
		this.box.matrix = rotWorldMatrix;
		this.box.rotation.setFromRotationMatrix(this.box.matrix);
	
		this.box.position.x = newPos.x;
		this.box.position.y = newPos.y;
		this.box.position.z = newPos.z;
	}
}


const vecX = new THREE.Vector3(1,0,0);
const vecY = new THREE.Vector3(0,1,0);
const vecZ = new THREE.Vector3(0,0,1);
const vectorAxis = {"x":vecX, "y":vecY, "z":vecZ}

class RubicGeometry {
	constructor(size) {
		this.size = parseInt(size) || 3;
		this.centerPivot = new THREE.Object3D;
		this.helper = new THREE.Object3D;
		this.geom = [];
		this.angle = 0;
		this.delta = 0.5-(size / 2);
		var x = 0;
		this.centerPivot.add(this.helper);
		while (x < size) {
			this.geom[x] = [];
			var y = 0;
			while (y < size) {
				this.geom[x][y] = [];
				var z = 0;
				while (z < size) {
					var elem = createRubicBox(x,y,z,size,this.delta);
					this.geom[x][y][z] = elem;
					if (elem) {
						this.centerPivot.add(elem.box);
					}
					z += 1;
				}
				y += 1;
			}
			x += 1;
		}
	}

	getGeom() {
		return this.centerPivot;
	}

	groupToPivot(axis,seg) {
		switch (axis) {
		case "x":
			this.helper.position.set(seg + this.delta,0,0);
			for (let y = 0; y < this.size; y++) {
				for (let z = 0; z < this.size; z++) {
					if (this.geom[seg][y][z]) {
						this.helper.add(this.geom[seg][y][z].box);
						this.geom[seg][y][z].box.position.x = 0;
					}
				}
			}
			break;
		case "y":
			this.helper.position.set(0,seg + this.delta,0);
			for (let x = 0; x < this.size; x++) {
				for (let z = 0; z < this.size; z++) {
					if (this.geom[x][seg][z]) {
						this.helper.add(this.geom[x][seg][z].box);
						this.geom[x][seg][z].box.position.y = 0;
					}
				}
			}
			break;
		case "z":
			this.helper.position.set(0,0,seg + this.delta);
			for (let x = 0; x < this.size; x++) {
				for (let y = 0; y < this.size; y++) {
					if (this.geom[x][y][seg]) {
						this.helper.add(this.geom[x][y][seg].box);
						this.geom[x][y][seg].box.position.z = 0;
					}
				}
			}
		}
	}

	ungroupFromPivot(axis, seg, direction) {
		let turnAngle = THREE.Math.degToRad(direction * 90);
		switch (axis) {
		case "x":
			for (let y = 0; y < this.size; y++) {
				for (let z = 0; z < this.size; z++) {
					if (this.geom[seg][y][z]) {
						this.centerPivot.add(this.geom[seg][y][z].box);
						this.geom[seg][y][z].globalRotation(new THREE.Vector3(1,0,0), turnAngle);
					}
				}
			}
			break;
		case "y":
			for (let x = 0; x < this.size; x++) {
				for (let z = 0; z < this.size; z++) {
					if (this.geom[x][seg][z]) {
						this.centerPivot.add(this.geom[x][seg][z].box);
						this.geom[x][seg][z].globalRotation(new THREE.Vector3(0,1,0), turnAngle);
					}
				}
			}
			break;
		case "z":
			for (let x = 0; x < this.size; x++) {
				for (let y = 0; y < this.size; y++) {
					if (this.geom[x][y][seg]) {
						this.centerPivot.add(this.geom[x][y][seg].box);
						this.geom[x][y][seg].globalRotation(new THREE.Vector3(0,0,1), turnAngle);
					}
				}
			}
		}
		this.helper.rotation.set(0,0,0);
	}

	setPositionBox() {
		for (let x = 0; x < this.size; x++) {
			for (let y = 0; y < this.size; y++) {
				for (let z = 0; z < this.size; z++) {
					if (this.geom[x][y][z]) {
						this.geom[x][y][z].box.position.set(x + this.delta, y + this.delta, z + this.delta);
					}
				}
			}
		}
	}

	rotateGeom(axis,segment,direction,delta){
		this.angle += delta * THREE.Math.degToRad(360 * direction);
		if (((direction == -1) && (this.angle > THREE.Math.degToRad(-90))) ||
		((direction == 1) && (this.angle < THREE.Math.degToRad(90))) ||
		((direction == -2) && (this.angle > THREE.Math.degToRad(-180))) ||
		((direction == 2) && (this.angle < THREE.Math.degToRad(180)))) {
			switch (axis) {
			case "x":
				this.helper.rotation.x = this.angle;
				break;
			case "y":
				this.helper.rotation.y = this.angle;
				break;
			case "z":
				this.helper.rotation.z = this.angle;
				break;
			}
			return false;
		} else {
			this.angle = 0;
			this.ungroupFromPivot(axis, segment, direction);
			this.recombination(axis,segment,direction);
			this.setPositionBox();
			return true;
		}
	}

	recombination_90(e, size) {
		let last = size - 1;
		for (let k = 0; k < last; k++) {
			let m = last - k;
			let t = e[k][0];
			e[k][0] = e[0][m];
			e[0][m] = e[m][last];
			e[m][last] = e[last][k];
			e[last][k] = t;
		}
		if ((last - 1) > 1) {
			var e2 = [];
			for (let i = 1; i < last; i++) {
				e2[i - 1] = [];
				for (let j = 1; j < last; j++) {
					e2[i - 1][j - 1] = e[i][j];
				} 
			}
			this.recombination_90(e2, (size - 2));
			for (let i = 1; i < last; i++) {
				for (let j = 1; j < last; j++) {
					e[i][j] = e2[i - 1][j - 1];
				} 
			}
		}
	}
	
	recombination(axis, seg, direction) {
		switch (axis) {
		case "x":
			switch (direction) {
			case -1:
				this.recombinationX(seg);
			case -2:
			case 2:
				this.recombinationX(seg);
			case 1:
				this.recombinationX(seg);
			}
			break;
		case "y":
			switch (direction) {
			case -1:
				this.recombinationY(seg);
			case -2:
			case 2:
				this.recombinationY(seg);
			case 1:
				this.recombinationY(seg);
			}
			break;
		case "z":
			switch (direction) {
			case -1:
				this.recombinationZ(seg);
			case -2:
			case 2:
				this.recombinationZ(seg);
			case 1:
				this.recombinationZ(seg);
			}
		}
	}

	recombinationX(seg) {
		this.recombination_90(this.geom[seg], this.size);
	}

	recombinationY(seg) {
		var e = [];
		for (let i = 0; i < this.size; i++) {
			e[i] = [];
			for (let j = 0; j < this.size; j++) {
				e[i][j] = this.geom[j][seg][i];
			}
		}
		this.recombination_90(e, this.size);
		for (let i = 0; i < this.size; i++) {
			for (let j = 0; j < this.size; j++) {
				this.geom[j][seg][i] = e[i][j];
			}
		}	
	}

	recombinationZ(seg) {
		var e = [];
		for (let i = 0; i < this.size; i++) {
			e[i] = [];
			for (let j = 0; j < this.size; j++) {
				e[i][j] = this.geom[i][j][seg];
			}
		}
		this.recombination_90(e, this.size);
		for (let i = 0; i < this.size; i++) {
			for (let j = 0; j < this.size; j++) {
				this.geom[i][j][seg] = e[i][j];
			}
		}	
	}
}

function createRubicBox(x,y,z,size, delta) {
	var side;
	var boxType;
	//TOP SIDE
	if (y == (size - 1)) {
		side = Side.Top;
		//FRONT EDGE
		if (z == 0) {
			//LEFT CORNER
			if (x == 0) {
				boxType = BoxType.CornerTopLeft;
			//RIGHT CORNER
			} else if (x == (size - 1)) {
				boxType = BoxType.CornerTopRight;
			//EDGE
			} else {
				boxType = BoxType.EdgeTop;
			}
		//BACK EDGE
		} else if (z == (size - 1)) {
			//LEFT CORNER
			if (x == 0) {
				boxType = BoxType.CornerBottomLeft;
			//RIGHT CORNER
			} else if (x == (size - 1)) {
				boxType = BoxType.CornerBottomRight;
			//EDGE
			} else {
				boxType = BoxType.EdgeBottom;
			}
		//LEFT EDGE
		} else if (x == 0) {
			boxType = BoxType.EdgeLeft;
		//RIGHT EDGE
		} else if (x == (size - 1)) {
			boxType = BoxType.EdgeRight;
		//CENTER
		} else {
			boxType = BoxType.Center;
		}
	//*
	//BOTTOM SIDE
	} else if (y == 0) {
		side = Side.Bottom;
		//FRONT EDGE
		if (z == (size - 1)) {
			//LEFT CORNER
			if (x == (size - 1)) {
				boxType = BoxType.CornerBottomLeft;
			//RIGHT CORNER
			} else if (x == 0) {
				boxType = BoxType.CornerBottomRight;
			//EDGE
			} else {
				boxType = BoxType.EdgeBottom;
			}
		//BACK EDGE
		} else if (z == 0) {
			//LEFT CORNER
			if (x == (size - 1)) {
				boxType = BoxType.CornerTopLeft;
			//RIGHT CORNER
			} else if (x == 0) {
				boxType = BoxType.CornerTopRight;
			//EDGE
			} else {
				boxType = BoxType.EdgeTop
			}
		//LEFT EDGE
		} else if (x == (size - 1)) {
			boxType = BoxType.EdgeLeft;
		//RIGHT EDGE
		} else if (x == 0) {
			boxType = BoxType.EdgeRight;
		//CENTER
		} else {
			boxType = BoxType.Center;
		}
	//*/
	//FRONT SIDE OR BACK SIDE
	} else if ((z == 0) || (z == (size - 1))) {
		if (z == 0) {
			side = Side.Back;
		} else {
			side = Side.Front;
		}
		//LEFT EDGE
		if (x == 0) {
			boxType = BoxType.EdgeLeft;
		//RIGHT EDGE
		} else if (x == (size - 1)) {
			boxType = BoxType.EdgeRight;
		//CENTER
		} else {
			boxType = BoxType.Center;
		}
	// LEFT OR RIGHT SIDE
	} else if ((x == 0) || (x == (size - 1))) {
		if (x == 0) {
			side = Side.Left;
		} else {
			side = Side.Right;
		}
		boxType = BoxType.Center;
	} else {
		return null;
	}
	//delta = 0.5-(size / 2);// + ((size % 2) * 0.5);
	return (new RubicBox(x, y, z, delta, boxType, side));
}


