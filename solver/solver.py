from solver.rubic import cube_t, rotateCube
from solver.top import solvTop
from solver.midl import solvMidl
from solver.bottom import solvBottom

def rotUpFace(cube):
	com = ["U", "U2", "U'", ""]
	sol = [0, 0, 0, 1]
	for i in range(4):
		rotateCube(cube, "U")
		for edge in range(4,8):
			ind = cube.ep.index(edge)
			if ind == edge:
				sol[i] += 2
				if cube.eo[ind] == 0:
					sol[i] += 1
		#print(cube.ep, sol)
	maxSol = max(sol)
	solv = com[sol.index(maxSol)]
	rotateCube(cube, solv)
	return solv

def restrictSolv(solv):
	dir = {	"U U'":"", "U U2":"U'", "U U":"U2", "U' U'":"U2", "U' U2":"U", "U' U":"", "U2 U":"U'", "U2 U2":"", "U2 U'":"U",
			"D D'":"", "D D2":"D'", "D D":"D2", "D' D'":"D2", "D' D2":"D", "D' D":"", "D2 D'":"D", "D2 D2":"", "D2 D":"D'",
			"F F'":"", "F F2":"F'", "F F":"F2", "F' F'":"F2", "F' F2":"F", "F' F":"", "F2 F'":"F", "F2 F2":"", "F2 F":"F'",
			"B B'":"", "B B2":"B'", "B B":"B2", "B' B'":"B2", "B' B2":"B", "B' B":"", "B2 B'":"B", "B2 B2":"", "B2 B":"B'",
			"L L'":"", "L L2":"L'", "L L":"L2", "L' L'":"L2", "L' L2":"L", "L' L":"", "L2 L'":"L", "L2 L2":"", "L2 L":"L'",
			"R R'":"", "R R2":"R'", "R R":"R2", "R' R'":"R2", "R' R2":"R", "R' R":"", "R2 R'":"R", "R2 R2":"", "R2 R":"R'",
			"  ":" "}
	for k, v in dir.items():
		solv = solv.replace(k, v)
	for k, v in dir.items():
		solv = solv.replace(k, v)
	return solv.strip()

def solver(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	#print(cube.ep)
	solv = restrictSolv(rotUpFace(cube).strip()+" "+solvTop(cube).strip()+" "+solvMidl(cube).strip() + " " + solvBottom(cube).strip()).strip()
	
	'''
	i8=cube.ep.index(8)
	i9=cube.ep.index(9)
	i10=cube.ep.index(10)
	i11=cube.ep.index(11)
	#print(cube.ep)
	print(cube.eo[8:])
	#print("[",cube.eo[i8],cube.eo[i9],cube.eo[i10],cube.eo[i11],"]")
	
	#print(findBottomCross(cube))
	s = ""
	for i in range(8, 12):
		s += str(cube.eo[cube.ep.index(i)])
	bc = findBottomCross(cube).strip()
	print(s,"[", bc, "]")
	#solv = solv+" "+bc
	'''
	f = ""
	s = ""
	for i in range(0,4):
		if i == cube.cp[i]:
			s += "0"
		else:
			s += "1"
			f += str(cube.cp[i])
	print(s, f)
	print(solv)

