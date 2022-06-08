from solver.rubic import cube_t, rotateCube

def findBottomCross(cube:cube_t):
	fm = ["F L D L' D' F'", "R F D F' D' R'", "B R D R' D' B'", "L B D B' D' L'"]
	com = {	"0000":"",
			"0011":str(fm[0]+" "+fm[0]),
			"0101":str(fm[1]),
			"0110":str(fm[1]+" "+fm[1]),
			"1001":str(fm[3]+" "+fm[3]),
			"1010":str(fm[2]),
			"1100":str(fm[2]+" "+fm[2]),
			"1111":str(fm[2]+" "+fm[0]+" "+fm[0])}
	s = ""
	for i in range(8,12):
		s += str(cube.eo[i])
	solv = com.get(s).strip()
	rotateCube(cube, solv)
	return solv

def rotBottomFace(cube):
	com = ["D", "D2", "D'", ""]
	sol = [0, 0, 0, 1]
	for i in range(4):
		rotateCube(cube, "D")
		for edge in range(8,12):
			ind = cube.ep.index(edge)
			if ind == edge:
				sol[i] += 2
				if cube.eo[ind] == 0:
					sol[i] += 1
	maxSol = max(sol)
	solv = com[sol.index(maxSol)]
	rotateCube(cube, solv)
	return solv.strip()

def findRightBottomCross(cube):
	com = { "0000": "",
		"0011":"L D L' F' L D L' D' L' F L2 D' L' D'",
		"0101":"L D L' F' L D L' D' L' F L2 D' L' D L D L' F' L D L' D' L' F L2 D' L' D2",
		"0110":"F D F' R' F D F' D' F' R F2 D' F' D'",
		"1001":"B D B' L' B D B' D' B' L B2 D' B' D'",
		"1010":"L D L' F' L D L' D' L' F L2 D' L' D L D L' F' L D L' D' L' F L2 D' L'",
		"1100":"R D R' B' R D R' D' R' B R2 D' R' D'"}
	s = ""
	for i in range(8,12):
		if i == cube.ep[i]:
			s += "0"
		else:
			s += "1"
	solv = str(com.get(s))
	rotateCube(cube, solv)
	return solv

def findBottomCorners(cube, corner):
	fm = ["D' R' D L D' R D L'", "D L D' R' D L' D' R", "D R D' L' D R' D' L", "D' L' D R D' L D R'"]
	dir = {	0:["", fm[0], fm[1], fm[2]],
			1:[fm[1], "", fm[3], fm[0]],
			2:[fm[2], fm[1], "", fm[3]],
			3:[fm[0], fm[3], fm[2], ""]}
	ind = cube.cp.index(corner)
	arr = dir.get(corner)
	solv = arr[ind]
	rotateCube(cube, solv)
	return solv

def rotateBottomCorners(cube):
	fm = "F' U' F U F' U' F U"
	solv = ""
	for i in range(0,4):
		while cube.co[2] != 0:
			rotateCube(cube, fm)
			solv += (" " + fm)
		rotateCube(cube, "D")
		solv += " D"
	return solv.strip()

def rotateBottomCorners2(cube):
	fm = "L' U L U' L' U L U'"
	solv = ""
	for i in range(0,4):
		while cube.co[3] != 0:
			rotateCube(cube, fm)
			solv += (" " + fm)
		rotateCube(cube, "D'")
		solv += " D'"
	return solv.strip()


def rotateDoubleSide(cube, s):
	dir = ["01", "12", "23", "30"]
	rot = ["D'", "", "D", "D2"]
	fm = "F L' F R2 F' L F R2 F2"
	pos = -1
	solv = ""
	for i in dir:
		pos = s.find(i)
		if pos != -1:
			break
	if pos == -1:
		if ((cube.cp[0] == 0)and(cube.cp[3]==3))or\
		((cube.cp[0] == 1) and (cube.cp[3]==0)) or\
		((cube.cp[0] == 2) and (cube.cp[3]==1)) or\
		((cube.cp[0] == 3) and (cube.cp[3]==2)):
			rotateCube(cube, "D2")
			solv = "D2"
		else:
			rotateCube(cube, fm)
			solv = fm
			for i in dir:
				pos = s.find(i)
				if pos != -1:
					break
	if pos != -1:
		solv = solv + " " + rot[pos] 
		solv = solv.strip() +" "+ fm
		rotateCube(cube, solv.strip())
	return solv.strip()

def checkEnd(cube):
	dir = {"0123":"", "1230":"D'", "2301":"D2","3012":"D"}
	s= "".join(map(str,cube.cp[:4]))
	com = dir.get(s)
	if com == None:
		return rotateDoubleSide(cube, s)
	else:
		rotateCube(cube, com)
		return com

def solvBottom(cube, corners):
	solv = findBottomCross(cube).strip()+" "+rotBottomFace(cube)
	solv = solv.strip() + " " + findRightBottomCross(cube).strip()
	
	for c in corners:
		solv = solv.strip() + " " + findBottomCorners(cube, c).strip()
	solv = solv.strip() + " " + rotateBottomCorners(cube).strip()
	return solv.strip()

def solvBottom2(cube):
	solv = rotateBottomCorners2(cube).strip()+" "+checkEnd(cube)
	solv = solv.strip() + " " + checkEnd(cube)
	solv = solv.strip() + " " + checkEnd(cube)
	return solv.strip()
