import sys
from solver.rubic import cube_t, rotateCube
from solver.top import findTopEdge, findTopCorner, solvTop
from solver.midl import findMidlEdge, solvMidl
from random import randint

RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
RES = "\033[0m"

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
		cube = cube_t()
		sc = randomScramble(cube)
		if (False == func(cube, sc)):
			errCount += 1
	if errCount == 0:
		print(GRN,"OK TEST!", name,RES)
	else:
		print(RED,"!!! NOT OK TEST",errCount,"FROM",testCount,"(",(errCount * 100 / testCount),"%)",YLW, name,RES)

 
#|==TESTS FOR FUNCTIONS==|

def testFindTopEdge(cube, sc, e=-1):
	edge = e
	if e == -1:
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

def testFindTopCorner(cube, sc, c=-1):
	corner = c
	if c == -1:
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

def testSolvTop(cube, sc, p=-1):
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

def testFindMidlEdge(cube, sc, e=-1):
	sc = sc + " " + solvTop(cube).strip()
	edge = e
	if e == -1:
		edge = randint(0,3)
	solv = findMidlEdge(cube, edge)
	ind = cube.ep.index(edge)
	flag = True
	if ind != edge:
		print(cube.ep)
		print("Error!: findMidlEdge for edge:", edge, "error position, scrabble[", sc, "] solv:[",solv,"]")
		flag = False
	else:
		if cube.eo[ind] == 1:
			print("Error!: findMidlEdge for edge:", edge, "error orientation, scrabble[", sc, "] solv:[",solv,"]")
			flag = False
	return flag

def testSolvMidl(cube, sc, p=-1):
	sc = sc + " " + solvTop(cube).strip()
	solv = solvMidl(cube).strip()
	flag = True
	for i in range(0,4):
		ind = cube.ep.index(i)
		if ind != i:
			print("Error!: solvMidl for edge:", i, " error position ", ind," scrabble: [", sc, "] solv:[",solv,"]")
			flag = False
		else:
			if cube.eo[ind] == 1:
				print("Error!: solvMidl for edge:", i, " error orientation, scrabble: [", sc, "] solv:[",solv,"]")
				flag = False
	return flag

#|========================|

def tests():
	testCount = 5000
	printFunctionTests(testFindTopEdge, "testFindTopEdge", testCount)
	printFunctionTests(testFindTopCorner, "testFindTopCorner", testCount)
	printFunctionTests(testSolvTop, "testSolvTop", testCount)
	printFunctionTests(testFindMidlEdge, "testFindMidlEdge", testCount)
	printFunctionTests(testSolvMidl, "testSolvMidl", testCount)

def individualTest(funcName, sc, param):
	cube = cube_t()
	if funcName in globals():
		func = globals()[funcName]
		if func(cube, sc, param):
			print(GRN,"Test OK!",RES)
		else:
			print(RED,"Test Not OK!",RES)
	else:
		print(RED,"Error! function",YLW, funcName,RED, "not found!",RES)

def main():
	if len(sys.argv) == 4:
		individualTest(sys.argv[1], sys.argv[2], int(sys.argv[3]))
	else:
		tests()
	exit(0)

main()