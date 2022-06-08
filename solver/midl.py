from solver.rubic import cube_t, rotateCube

def findMidlEdge(cube:cube_t, edge:int):

	fm = [	["D' R' D R D F D' F'", "D L D' L' D' F' D F"],
			["D' L' D L D B D' B'", "D R D' R' D' B' D B"],
			["D' F' D F D L D' L'", "D B D' B' D' L' D L"],
			["D' B' D B D R D' R'", "D F D' F' D' R' D R"]]

	dir = {	0:[	["",						fm[1][0]+" D2 "+fm[1][0]],
				[fm[3][0]+" D' "+fm[1][0],	fm[1][1]+" D2 "+fm[1][0]],
				[fm[3][1]+" D' "+fm[1][0],	fm[0][0]+ " " + fm[1][0]],
				[fm[2][0]+" D "+ fm[1][0],	fm[0][1]+ " " + fm[1][0]],
				[],[],[],[],
				[fm[1][0],					"D "+ fm[2][1]],
				["D "+ fm[1][0],			"D2 "+fm[2][1]],
				["D2 "+fm[1][0],			"D' "+fm[2][1]],
				["D' "+fm[1][0],			fm[2][1]]],
			1:[	[fm[2][1]+" D "+ fm[1][1],	fm[1][0]+" D2 "+fm[1][1]],
				["",						fm[1][1]+" D2 "+fm[1][1]],
				[fm[3][1]+" D' "+fm[1][1],	fm[0][0]+ " " + fm[1][1]],
				[fm[2][0]+" D "+ fm[1][1],	fm[0][1]+ " " + fm[1][1]],
				[],[],[],[],
				[fm[1][1],					"D' "+fm[3][0]],
				["D "+ fm[1][1],			fm[3][0]],
				["D2 "+fm[1][1],			"D "+fm[3][0]],
				["D' "+fm[1][1],			"D2 "+fm[3][0]]],
			2:[	[fm[2][1]+" D' "+fm[0][0],	fm[1][0]+ " " + fm[0][0]],
				[fm[3][0]+" D "+ fm[0][0],	fm[1][1]+ " " + fm[0][0]],
				["",						fm[0][0]+" D2 "+fm[0][0]],
				[fm[2][0]+" D' "+fm[0][0],	fm[0][1]+" D2 "+fm[0][0]],
				[],[],[],[],
				["D2 "+fm[0][0],			"D' "+fm[3][1]],
				["D' "+fm[0][0],			fm[3][1]],
				[fm[0][0],					"D "+fm[3][1]],
				["D "+fm[0][0],				"D2 "+fm[3][1]]],	
			3:[	[fm[2][1]+" D' "+fm[0][1],	fm[1][0]+ " " + fm[0][1]],
				[fm[3][0]+" D "+ fm[0][1],	fm[1][1]+ " " + fm[0][1]],
				[fm[3][1]+" D "+ fm[0][1],	fm[0][0]+" D2 "+fm[0][1]],
				["",						fm[0][1]+" D2 "+fm[0][1]],
				[],[],[],[],
				["D2 "+fm[0][1],			"D "+fm[2][0]],
				["D' "+fm[0][1],			"D2 "+fm[2][0]],
				[fm[0][1],					"D' "+fm[2][0]],
				["D "+fm[0][1],				fm[2][0]]]}
	ind = cube.ep.index(edge)
	rot = cube.eo[ind]
	arr = dir.get(edge)
	solv = arr[ind][rot]
	rotateCube(cube, solv)
	return solv

def solvMidl(cube:cube_t, edges):
	
	solv = ""
	for e in edges:
		solv = solv.strip() + " " + findMidlEdge(cube, e).strip()
	return solv.strip()
