from solver.rubic import cube_t, rotateCube

def findBottomCross(cube:cube_t):
	fm = ["F L D L' D' F'", "R F D F' D' R'", "B R D R' D' B'", "L B D B' D' L'"]
	com = {    "0000":"",
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
	solv = com.get(s).strip()
	rotateCube(cube, solv)
	return solv

def solvBottom(cube):
	solv = findBottomCross(cube).strip()+" "+rotBottomFace(cube)
	solv = solv.strip() + " " + findRightBottomCross(cube).strip()
	return solv.strip()





	