from enum import Enum
from typing import NewType

class cube_t:
	def __init__(self):
		self.cp:[int] = [i for i in range(8)]
		self.co:[int] = [0] * 8
		self.ep:[int] = [i for i in range(12)]
		self.eo:[int] = [0] * 12

	def rotate(self, face:int, count:int = 1):
		if (face < 0) or (face > 5):
			return
		corner_rotate_map = [
		[[4, 5, 6, 7], [3, 2, 1, 0], [7, 6, 2, 3], [5, 4, 0, 1], [4, 7, 3, 0], [6, 5, 1, 2]],
		[[7, 6, 5, 4], [0, 1, 2, 3], [7, 3, 2, 6], [5, 1, 0, 4], [4, 0, 3, 7], [6, 2, 1, 5]]]
		edge_rotate_map = [
		[[4, 5, 6, 7], [11, 10, 9, 8], [6, 2, 10, 3], [4, 0, 8, 1], [7, 3, 11, 0], [5, 1, 9, 2]],
		[[7, 6, 5, 4], [8, 9, 10, 11], [3, 10, 2, 6], [1, 8, 0, 4], [0, 11, 3, 7], [2, 9, 1, 5]]]
		def swap(A, C):
			tmp = A[C[3]]
			A[C[3]] = A[C[2]]
			A[C[2]] = A[C[1]]
			A[C[1]] = A[C[0]]
			A[C[0]] = tmp
		count = (count % 4 + 4) & 3
		if count == 2:
			C = corner_rotate_map[0][face]
			self.cp[C[0]], self.cp[C[2]] = self.cp[C[2]], self.cp[C[0]]
			self.cp[C[1]], self.cp[C[3]] = self.cp[C[3]], self.cp[C[1]]
			self.co[C[0]], self.co[C[2]] = self.co[C[2]], self.co[C[0]]
			self.co[C[1]], self.co[C[3]] = self.co[C[3]], self.co[C[1]]

			E = edge_rotate_map[0][face]
			self.ep[E[0]], self.ep[E[2]] = self.ep[E[2]], self.ep[E[0]]
			self.ep[E[1]], self.ep[E[3]] = self.ep[E[3]], self.ep[E[1]]
			self.eo[E[0]], self.eo[E[2]] = self.eo[E[2]], self.eo[E[0]]
			self.eo[E[1]], self.eo[E[3]] = self.eo[E[3]], self.eo[E[1]]
		else:
			C = corner_rotate_map[count >> 1][face]
			swap(self.cp, C)
			swap(self.co, C)
			if face >= 2:
				self.co[C[0]] += 1
				self.co[C[2]] += 1
				self.co[C[1]] -= 1
				self.co[C[3]] -= 1
				if self.co[C[0]] == 3:
					self.co[C[0]] = 0
				if self.co[C[2]] == 3:
					self.co[C[2]] = 0
				if self.co[C[1]] == -1:
					self.co[C[1]] = 2
				if self.co[C[3]] == -1:
					self.co[C[3]] = 2
			E = edge_rotate_map[count >> 1][face]
			flag = False
			if face >= 4:
				self.eo[E[0]] ^= 1
				self.eo[E[1]] ^= 1
				self.eo[E[2]] ^= 1
				self.eo[E[3]] ^= 1
			swap(self.ep, E)
			swap(self.eo, E)

def commandToArray(c):
	dicFace = { "R":5, "L":4, "D":1, "U":0, "F":2, "B":3 }
	dicDir = { "'":3, "2":2 }
	return list(map(lambda c: (dicFace.get(c[0], -1), dicDir.get(c[-1], 1)), c.split()))

def rotateCube(cube:cube_t, command):
	arr = commandToArray(command)
	for a in arr:
		if a[0] is None:
			return
		cube.rotate(a[0], a[1])
