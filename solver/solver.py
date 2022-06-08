from solver.rubic import cube_t, rotateCube
from solver.top import solvTop, solvTop2
from solver.midl import solvMidl
from solver.bottom import solvBottom, solvBottom2

def restrictSolv(solv):
	dir = {	"U U'":"", "U U2":"U'", "U U":"U2", "U' U'":"U2", "U' U2":"U", "U' U":"", "U2 U":"U'", "U2 U2":"", "U2 U'":"U",
			"D D'":"", "D D2":"D'", "D D":"D2", "D' D'":"D2", "D' D2":"D", "D' D":"", "D2 D'":"D", "D2 D2":"", "D2 D":"D'",
			"F F'":"", "F F2":"F'", "F F":"F2", "F' F'":"F2", "F' F2":"F", "F' F":"", "F2 F'":"F", "F2 F2":"", "F2 F":"F'",
			"B B'":"", "B B2":"B'", "B B":"B2", "B' B'":"B2", "B' B2":"B", "B' B":"", "B2 B'":"B", "B2 B2":"", "B2 B":"B'",
			"L L'":"", "L L2":"L'", "L L":"L2", "L' L'":"L2", "L' L2":"L", "L' L":"", "L2 L'":"L", "L2 L2":"", "L2 L":"L'",
			"R R'":"", "R R2":"R'", "R R":"R2", "R' R'":"R2", "R' R2":"R", "R' R":"", "R2 R'":"R", "R2 R2":"", "R2 R":"R'",
			"  ":" "}
	flag = True
	while flag == True:
		newSolv = solv
		for k, v in dir.items():
			newSolv = newSolv.replace(k, v)
		if newSolv == solv:
			flag = False
		solv = newSolv
	return solv.strip()

def solver3(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	x1 = cube.copy()
	solv1 = restrictSolv(solvTop(cube,[4,5,6,7],[4,5,6,7]).strip()+" "+solvMidl(cube,[0,1,2,3]).strip()+" "+solvBottom(cube,[0,1,2,3]).strip()).strip()
	solv2 = restrictSolv(solvTop(x1,[4,7,6,5],[7,6,5,4]).strip()+" "+solvMidl(x1,[0,1,2,3]).strip()+" "+solvBottom(x1,[0,1,2,3]).strip()).strip()
	if len(solv1)>len(solv2)
		print(solv1)
		else print(solv2)

def solver2(a):
	cube = cube_t()
	rotateCube(cube, a.upper())
	solv = restrictSolv(solvTop2(cube).strip()+" "+solvBottom2(cube).strip()).strip()
	print(solv)
