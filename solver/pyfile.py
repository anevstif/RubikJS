from solver.rubic import cube_t, face_type


def solver2(a):
	dic = { "R":"R\'", "R'":"R",
			"L":"L\'", "L'":"L",
			"D":"D\'", "D'":"D",
			"U":"U\'", "U'":"U",
			"F":"F\'", "F'":"F",
			"B":"B\'", "B'":"B" }
	arr  = a.split()
	newArr = list(map(lambda c: dic.get(c, c), arr))
	arr = newArr[::-1]
	solv = (" ").join(arr)
	cube = cube_t()
	print(cube.cp)
	print(solv)

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
		#ind = cube.ep.index(4)
		#print("(",a[0].value, ";", a[1], "):[", cube.eo[ind], "]")

def findCrossEdge(cube, edge):
	dir = {
		4:["B'", "B", "F D2 F' B2", "F' D2 F B2", "", "R2 D B2", "F2 D2 B2", "L2 D' B2", "B2", "D B2", "D2 B2", "D' B2", "B U' L U"],
		5:["B D' B' R2", "R'", "R", "L D2 L' R2", "B2 D' R2", "", "U", "F2 D R2", "L2 D2 R2", "R2", "D R2", "D2 R2", "R U' B U"],
		6:["L' D F2", "R D' F2", "F'", "F", "B2 D2 F2", "R2 D' F2", "", "L2 D F2", "D2 F2", "D' F2", "F2", "D F2", "F U' R U"],
		7:["L", "R D2 R' L2", "F D' F' L2", "L'", "B2 D L2", "R2 D2 L2", "F2 D' L2", "", "D L2", "D2 L2", "D' L2", "L2", "L U' F U"]}
	arr = dir.get(edge)
	ind = cube.ep.index(edge)
	solv = arr[ind]
	print("edge=", edge, " index=", ind, " solv=" + solv)
	rotateCube(cube, solv)
	if cube.eo[edge] == 1:
		addSolv = arr[12]
		rotateCube(cube, addSolv)
		solv = solv + " " + addSolv
	return solv

def findCrossCorner(cube, corner):
	dir = {
		4:["L' D' L D", "D L' D' L D", "D2 L' D' L D", "D' L' D' L D", "", "B' D' B D2 L' D' L D", "R' D' R D' L' D' L D", "F' D' F L' D' L D", "L' D' L D L' D' L D"],
		5:["", "", "", "", "", "", "", ""],
		6:["", "", "", "", "", "", "", ""],
		7:["", "", "", "", "", "", "", ""]}
	}

def solvCross(cube):
	solv = findCrossEdge(cube, 4).strip()
	#print(solv)
	solv = solv.strip() + " " + findCrossEdge(cube, 5).strip()
	#print(solv)
	solv = solv.strip() + " " + findCrossEdge(cube, 6).strip()
	#print(solv)
	solv = solv.strip() + " " + findCrossEdge(cube, 7).strip()
	return solv

def restrictSolv(solv):
	dir = {
		"U U":"U2",
		"U U'":"",
		"U U2":"U'",
		"U' U":"",
		"U' U'":"U2",
		"U' U2":"U",
		"U2 U":"U'",
		"U2 U'":"U",
		"U2 U2":"",
		"D D":"D2",
		"D D'":"",
		"D D2":"D'",
		"D' D":"",
		"D' D'":"D2",
		"D' D2":"D",
		"D2 D":"D'",
		"D2 D'":"D",
		"D2 D2":"",
		"F F":"F2",
		"F F'":"",
		"F F2":"F'",
		"F' F":"",
		"F' F'":"F2",
		"F' F2":"F",
		"F2 F":"F'",
		"F2 F'":"F",
		"F2 F2":"",
		"B B":"B2",
		"B B'":"",
		"B B2":"B'",
		"B' B":"",
		"B' B'":"B2",
		"B' B2":"B",
		"B2 B":"B'",
		"B2 B'":"B",
		"B2 B2":"",
		"L L":"L2",
		"L L'":"",
		"L L2":"L'",
		"L' L":"",
		"L' L'":"L2",
		"L' L2":"L",
		"L2 L":"L'",
		"L2 L'":"L",
		"L2 L2":"",
		"R R":"R2",
		"R R'":"",
		"R R2":"R'",
		"R' R":"",
		"R' R'":"R2",
		"R' R2":"R",
		"R2 R":"R'",
		"R2 R'":"R",
		"R2 R2":"",
	}
	for k, v in dir.items():
		solv = solv.replace(k, v)
	return solv

def solver(a):
	cube = cube_t()
	#print("block=",cube.getBlock(2, 0, 1))
	#print(cube.ep)
	rotateCube(cube, a)
	#print(cube.ep)
	solv = restrictSolv(solvCross(cube).strip())
	#print("solv=", solv)
	#rotateCube(cube, solv)
	#if cube.eo[4] == 1:
	#	rotateCube(cube, "B U' L U")
	#	solv  = "" if solv == "" else solv + " "
	#	solv += "B U' L U"
	print(solv)
	#print(cube.ep)

	
