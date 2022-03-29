from solver.rubic import cube_t, face_type

def commandToArray(c):
	dicFace = { 
		"R":face_type.right,
		"L":face_type.left,
		"D":face_type.bottom,
		"U":face_type.top,
		"F":face_type.front,
		"B":face_type.back }
	dicDir = {
		"'":3,
		"2":2,
	}
	return list(map(lambda c: (dicFace.get(c[0], None), dicDir.get(c[-1], 1)), c.split()))

def rotateCube(cube, command):
	arr = commandToArray(command)
	for a in arr:
		if a[0] is None:
			return
		cube.rotate(a[0], a[1])

def findCrossEdge(cube, edge):
	dir = {
		4:["B'", "B", "F D2 F' B2", "F' D2 F B2", "", "R2 D B2", "F2 D2 B2", "L2 D' B2", "B2", "D B2", "D2 B2", "D' B2", "B U' L U"],
		5:["B D' B' R2", "R'", "R", "L D2 L' R2", "B2 D' R2", "", "F2 D R2", "L2 D2 R2", "D' R2", "R2", "D R2", "D2 R2", "R U' B U"],
		6:["L' D F2", "R D' R' F2", "F'", "F", "B2 D2 F2", "R2 D' F2", "", "L2 D F2", "D2 F2", "D' F2", "F2", "D F2", "F U' R U"],
		7:["L", "R D2 R' L2", "F D' F' L2", "L'", "B2 D L2", "R2 D2 L2", "F2 D' L2", "", "D L2", "D2 L2", "D' L2", "L2", "L U' F U"]}
	arr = dir.get(edge)
	ind = cube.ep.index(edge)
	solv = arr[ind]
	rotateCube(cube, solv)
	if cube.eo[edge] == 1:
		addSolv = arr[12]
		rotateCube(cube, addSolv)
		solv = solv + " " + addSolv
	return solv

def findCrossCorner(cube, corner):
	dir = {
		4:["", "D", "D2", "D'", "", "B' D' B D2", "R' D2 R'", "F' D' F", "L' D' L D"],
		5:["D'", "", "D", "D2", "L' D' L", "", "R' D' R D2", "F' D2 F", "B' D' B D"],
		6:["D2", "D'", "", "D", "L' D2 L", "B' D' B", "", "F' D' F D2", "R' D' R D"],
		7:["D", "D2", "D'", "", "L' D' L D2", "B' D2 B", "R' D' R", "", "F' D' F D"]}
	arr = dir.get(corner)
	ind = cube.cp.index(corner)
	solv = ""
	if corner != ind:
		solv = arr[ind] + " " + arr[8]
		rotateCube(cube, solv)
	err = 0
	ind = cube.cp.index(corner)
	while cube.co[ind] != 0:
		revert = arr[8] + " " + arr[8]
		solv = solv + " " + revert
		rotateCube(cube, revert)
		err += 1
		if err == 3:
			return ""
	return solv.strip()

def solvCross(cube):
	edges = [4,5,6,7]
	corners = [4,5,6,7]
	solv = ""
	for e in edges:
		solv = solv.strip() + " " + findCrossEdge(cube, e).strip()
	for c in corners:
		solv = solv.strip() + " " + findCrossCorner(cube, c).strip()
	return solv.strip()

def restrictSolv(solv):
	dir = {
		"U U'":"",
		"U U2":"U'",
		"U U":"U2",
		"U' U'":"U2",
		"U' U2":"U",
		"U' U":"",
		"U2 U":"U'",
		"U2 U2":"",
		"U2 U'":"U",
		"D D'":"",
		"D D2":"D'",
		"D D":"D2",
		"D' D'":"D2",
		"D' D2":"D",
		"D' D":"",
		"D2 D'":"D",
		"D2 D2":"",
		"D2 D":"D'",
		"F F'":"",
		"F F2":"F'",
		"F F":"F2",
		"F' F'":"F2",
		"F' F2":"F",
		"F' F":"",
		"F2 F'":"F",
		"F2 F2":"",
		"F2 F":"F'",
		"B B'":"",
		"B B2":"B'",
		"B B":"B2",
		"B' B'":"B2",
		"B' B2":"B",
		"B' B":"",
		"B2 B'":"B",
		"B2 B2":"",
		"B2 B":"B'",
		"L L'":"",
		"L L2":"L'",
		"L L":"L2",
		"L' L'":"L2",
		"L' L2":"L",
		"L' L":"",
		"L2 L'":"L",
		"L2 L2":"",
		"L2 L":"L'",
		"R R'":"",
		"R R2":"R'",
		"R R":"R2",
		"R' R'":"R2",
		"R' R2":"R",
		"R' R":"",
		"R2 R'":"R",
		"R2 R2":"",
		"R2 R":"R'",
		"  ":" "
	}
	for k, v in dir.items():
		solv = solv.replace(k, v)
	for k, v in dir.items():
		solv = solv.replace(k, v)
	return solv.strip()

def solver(a):
	cube = cube_t()
	rotateCube(cube, a)

	solv = restrictSolv(solvCross(cube))
	print(solv)
