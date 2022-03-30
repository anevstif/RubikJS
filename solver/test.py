from solver.rubic import cube_t, rotateCube
from solver.top import findTopEdge, findTopCorner, solvTop
from solver.midl import findMidlEdge, solvMidl
from random import randint

def randomScramble(cube:cube_t):
	face = ["U", "D", "F", "B", "L", "R"]
	dir = ["", "2", "'"]
	m = randint(1, 100)
	s = ""
	for i in range(0, m):
		s += face[randint(0, 5)]+dir[randint(0,2)]+" "
	s = s.strip()
	rotateCube(cube, s)
	return s

def testFindTopEdge():
	cube = cube_t()
	sc = randomScramble(cube)
	edge = randint(4,7)
	findTopEdge(cube, edge)
	ind = cube.ep.index(edge)
	flag = True
	if ind != edge:
		print("Error!: findTopEdge for edge:", edge, "error position, scrabble[", sc, "]")
		flagErr = False
	else:
		if cube.eo[ind] == 1:
			print("Error!: findTopEdge for edge:", edge, "error orientation, scrabble[", sc, "]")
			flagErr = False
	return flag

def testFindTopCorner():
	cube = cube_t()
	sc = randomScramble(cube)
	corner = randint(4,7)
	findTopCorner(cube, corner)
	ind = cube.cp.index(corner)
	flag = True
	if ind != corner:
		print("Error!: findTopCorner for corner:", corner, " error position, scrabble: [", sc, "]")
		flag = False
	else:
		if cube.co[ind] == 1:
			print("Error!: findTopEdge for corner:", corner, " error orientation, scrabble: [", sc, "]")
			flag = False
	return flag

def testSolvTop():
	cube = cube_t()
	sc = randomScramble(cube)
	solv = solvTop(cube)
	rotateCube(cube, solv)
	flag = True
	for i in range(4,8):
		ind = cube.ep.index(i)
		if ind != i:
			print("Error!: solvTop for edge:", i, " error position ", ind," scrabble: [", sc, "]")
			flag = False
		else:
			if cube.eo[ind] == 1:
				print("Error!: solvTop for edge:", i, " error orientation, scrabble: [", sc, "]")
				flag = False
		ind = cube.cp.index(i)
		if ind != i:
			print("Error!: solvTop for corner:", i, " error position ", ind," scrabble: [", sc, "]")
			flag = False
		else:
			if cube.co[ind] == 1:
				print("Error!: solvTop for corner:", i, " error orientation, scrabble: [", sc, "]")
				flag = False
	return flag



def printFunctionTests(func, name, testCount):
	flag = True
	for i in range(0, testCount):
		flag = flag and func()
	if flag:
		print("OK TEST!", name)
	else:
		print("NOT OK TEST!", name)

def tests():
	testCount = 1000
	printFunctionTests(testFindTopEdge, "testFindTopEdge", testCount)
	printFunctionTests(testFindTopCorner, "testFindTopCorner", testCount)
	printFunctionTests(testSolvTop, "testSolvTop", testCount)