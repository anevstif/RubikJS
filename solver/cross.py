from solver.rubic import cube_t, rotateCube

def findCrossEdge(cube:cube_t, edge:int):
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

def findCrossCorner(cube:cube_t, corner:int):
	dir = {
		4:["", "D", "D2", "D'", "", "B' D' B D2", "R' D2 R", "F' D' F", "L' D' L D"],
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

def solvCross(cube:cube_t):
	edges = [4,5,6,7]
	corners = [4,5,6,7]
	solv = ""
	for e in edges:
		solv = solv.strip() + " " + findCrossEdge(cube, e).strip()
		#print("[",solv, "]")
	for c in corners:
		solv = solv.strip() + " " + findCrossCorner(cube, c).strip()
		#print("[",solv, "]")
	return solv.strip()
