from solver.rubic import cube_t, rotateCube
from solver.top import findTopEdge, findTopCorner, solvTop
from solver.midl import findMidlEdge, solvMidl
from random import randint

def randomScramble(cube):
	face = ["U", "D", "F", "B", "L", "R"]
	dir = ["", "2", "'"]
	m = randint(1, 100)
	s = ""
	for i in range(0, m):
		s += face[randint(0, 5)]+dir[randint(0,2)]+" "
	s = s.strip()
	rotateCube(cube, s)
	return s

def printFunctionTests(func, name, testCount):
	errCount = 0
	for i in range(0, testCount):
		if (False == func()):
			errCount += 1
	if errCount == 0:
		print("\033[32m","OK TEST!", name,"\033[0m")
	else:
		print("\033[31m","!!! NOT OK TEST",errCount,"FROM",testCount,"(",(errCount * 100 / testCount),"%)","\033[33m", name,"\033[0m")

 
#|==TESTS FOR FUNCTIONS==|

def testFindTopEdge():
	cube = cube_t()
	sc = randomScramble(cube)
	edge = randint(4,7)
	solv = findTopEdge(cube, edge)
	ind = cube.ep.index(edge)
	flag = True
	if ind != edge:
		print("Error!: findTopEdge for edge:", edge, "error position, scrabble[", sc, "] solv:[",solv,"]")
		flag = False
	else:
		if cube.eo[ind] == 1:
			print("Error!: findTopEdge for edge:", edge, "error orientation, scrabble[", sc, "] solv:[",solv,"]")
			flag = False
	return flag

def testFindTopCorner():
	cube = cube_t()
	sc = randomScramble(cube)
	corner = randint(4,7)
	solv = findTopCorner(cube, corner)
	ind = cube.cp.index(corner)
	flag = True
	if ind != corner:
		print("Error!: findTopCorner for corner:", corner, " error position, scrabble: [", sc, "] solv:[",solv,"]")
		flag = False
	else:
		if cube.co[ind] == 1:
			print("Error!: findTopEdge for corner:", corner, " error orientation, scrabble: [", sc, "] solv:[",solv,"]")
			flag = False
	return flag

def testSolvTop():
	cube = cube_t()
	sc = randomScramble(cube)
	solv = solvTop(cube).strip()
	flag = True
	for i in range(4,8):
		ind = cube.ep.index(i)
		if ind != i:
			print("Error!: solvTop for edge:", i, " error position ", ind," scrabble: [", sc, "] solv:[",solv,"]")
			flag = False
		else:
			if cube.eo[ind] == 1:
				print("Error!: solvTop for edge:", i, " error orientation, scrabble: [", sc, "] solv:[",solv,"]")
				flag = False
		ind = cube.cp.index(i)
		if ind != i:
			print("Error!: solvTop for corner:", i, " error position ", ind," scrabble: [", sc, "] solv:[",solv,"]")
			flag = False
		else:
			if cube.co[ind] == 1:
				print("Error!: solvTop for corner:", i, " error orientation, scrabble: [", sc, "] solv:[",solv,"]")
				flag = False
	return flag

def testFindMidlEdge():
	cube = cube_t()
	sc = randomScramble(cube)
	solvTop(cube)
	edge = randint(0,3)
	solv = findMidlEdge(cube, edge)
	ind = cube.ep.index(edge)
	flag = True
	if ind != edge:
		print("Error!: findTopEdge for edge:", edge, "error position, scrabble[", sc, "] solv:[",solv,"]")
		flag = False
	else:
		if cube.eo[ind] == 1:
			print("Error!: findTopEdge for edge:", edge, "error orientation, scrabble[", sc, "] solv:[",solv,"]")
			flag = False
	return flag

#|========================|

def tests():
	testCount = 1000
	printFunctionTests(testFindTopEdge, "testFindTopEdge", testCount)
	printFunctionTests(testFindTopCorner, "testFindTopCorner", testCount)
	printFunctionTests(testSolvTop, "testSolvTop", testCount)
	printFunctionTests(testFindMidlEdge, "testFindMidlEdge", testCount)
	exit(0)

tests()