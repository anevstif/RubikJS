import sys
from solver.rubic import cube_t, rotateCube
from solver.top import findTopEdge, findTopCorner, solvTop, solvTop2
from solver.midl import findMidlEdge, solvMidl
from solver.bottom import rotBottomFace, findBottomCross, findRightBottomCross, solvBottom, solvBottom2
from random import randint

RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
RES = "\033[0m"

def randomScramble(cube):
	face = ["U", "D", "F", "B", "L", "R"]
	dir = ["", "2", "'"]
	m = randint(1, 200)
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

def printError(funcName, elem, elemNumber, character, characterNumber, scramble, solver):
	print("Error!:",funcName,"for",elem,":",elemNumber, " error",character, characterNumber," scrabble: [", scramble, "] solv:[",solver,"]")
 
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

def testSolvTop2(cube, sc, p=-1):
	solv = solvTop2(cube).strip()
	flag = True
	for i in range(4,8):
		ind = cube.cp.index(i)
		if ind != i:
			print("Error!: solvTop2 for corner:", i, " error position ", ind," scrabble: [", sc, "] solv:[",solv,"]")
			flag = False
		else:
			if cube.co[ind] == 1:
				print("Error!: solvTop2 for corner:", i, " error orientation, scrabble: [", sc, "] solv:[",solv,"]")
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
			printError("solvMidl","edge:",i,"position",ind,sc,solv)
			flag = False
		else:
			if cube.eo[ind] == 1:
				printError("solvMidl","edge:",i,"orientation",ind,sc,solv)
				flag = False
	return flag

def testFindBottomCross(cube, sc, p=-1):
	sc = sc + " " + solvTop(cube).strip() + " " + solvMidl(cube).strip()
	solv = findBottomCross(cube)
	flag = True
	s = ""
	for i in range(8, 12):
		s += str(cube.eo[i])
	if s != "0000":
		printError("findBottomCross","edge:","[",s,"]",sc,solv)
		flag = False
	return flag

def testFindRightBottomCross(cube, sc, p=-1):
	sc = sc + " " + solvTop(cube).strip() + " " + solvMidl(cube).strip()
	sc = sc.strip() + " "+findBottomCross(cube)
	sc = sc.strip() + " "+rotBottomFace(cube)
	solv = findRightBottomCross(cube)
	flag = True
	s = ""
	for i in range(8, 12):
		s += str(cube.ep[i])
	if s != "891011":
		printError("findRightBottomCross","edge:","","position","",sc,solv)
		flag = False
	s = ""
	for i in range(8, 12):
		s += str(cube.eo[i])
	if s != "0000":
		printError("findRightBottomCross","edge:","","orientation","",sc,solv)
		flag = False
	return flag

def testSolvBottom(cube, sc, p=-1):
	sc = sc + " " + solvTop(cube).strip()
	sc = sc.strip() + " " + solvMidl(cube).strip()
	solv = solvBottom(cube).strip()
	flag = True
	for i in range(8,12):
		ind = cube.ep.index(i)
		if ind != i:
			printError("solvBottom","edge:",i,"position",ind,sc,solv)
			flag = False
		else:
			if cube.eo[ind] == 1:
				printError("solvBottom","edge:",i,"orientation",ind,sc,solv)
				flag = False
	for i in range(0,4):
		ind = cube.cp.index(i)
		if ind != i:
			printError("solvBottom","corner:",i,"position",ind,sc,solv)
			flag = False
		else:
			if cube.co[ind] == 1:
				printError("solvBottom","corner:",i,"orientation",ind,sc,solv)
				flag = False
	return flag

def testSolvBottom2(cube, sc, p=-1):
	#sc = sc + " " + solvTop2(cube).strip()
	#sc = sc.strip() + " " + solvMidl(cube).strip()
	#sc = sc.strip() + " " + rotBottomFace(cube)
	#sc = sc.strip() + " " + findRightBottomCross(cube).strip()

	#rotateCube(cube, sc.upper())
	#solv = (solvTop2(cube).strip()+" "+solvBottom2(cube).strip()).strip()

	#solv = solvBottom2(cube).strip()
	
	sc = sc + " " + solvTop2(cube).strip()
	solv = solvBottom2(cube).strip()
	#print(cube.cp[:4])
	
	flag = True
	for i in range(0,4):
		ind = cube.cp.index(i)
		if ind != i:
			printError("solvBottom2","corner:",i,"position",ind,sc,solv)
			flag = False
		else:
			if cube.co[ind] == 1:
				printError("solvBottom2","corner:",i,"orientation",ind,sc,solv)
				flag = False
	return flag

#|========================|

def tests():
	testCount = 1000
	printFunctionTests(testFindTopEdge, "testFindTopEdge", testCount)
	printFunctionTests(testFindTopCorner, "testFindTopCorner", testCount)
	printFunctionTests(testSolvTop, "testSolvTop", testCount)
	printFunctionTests(testFindMidlEdge, "testFindMidlEdge", testCount)
	printFunctionTests(testSolvMidl, "testSolvMidl", testCount)
	printFunctionTests(testFindBottomCross, "testFindBottomCross", testCount)
	printFunctionTests(testFindRightBottomCross, "testFindRightBottomCross", testCount)
	printFunctionTests(testSolvBottom, "testSolvBottom", testCount)
	printFunctionTests(testSolvTop2, "testSolvTop2", testCount)
	printFunctionTests(testSolvBottom2, "testSolvBottom2", testCount)

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