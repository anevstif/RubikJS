from enum import Enum
from typing import NewType

face_type = Enum('face_type', 'top bottom front back left right', start = 0)

class face_t:
	def __init__(self):
		self.C:[int] = [9]


class block_t:
	def __init__(self, f:[int]):
		self.top:int = f[0]
		self.bottom:int = f[1]
		self.front:int= f[2]
		self.back:int = f[3]
		self.left:int = f[4]
		self.right:int = f[5]
	def __str__(self):
		return "[t=" + str(self.top) + " b=" + str(self.bottom) + " f=" + str(self.front) + " b=" + str(self.back) + " l=" + str(self.left) + " r=" + str(self.right) + "]"

block_info_t = NewType('block_info_t', (int, int))

class cube_t:
	def __init__(self):
		self.cp:[int] = [i for i in range(8)]
		self.co:[int] = [0] * 8
		self.ep:[int] = [i for i in range(12)]
		self.eo:[int] = [0] * 12

	def getCornerBlock(self)->block_info_t:
		b: block_info_t = (self.cp, self.co)
		return b

	def getEdgeBlock(self)->block_info_t:
		b: block_info_t = (self.ep, self.eo)
		return b

	def rotate(self, type:face_type, count:int = 1):
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
		def swap2(a, b):
			t = a
			a = b
			b = t
		count = (count % 4 + 4) & 3
		if count == 2:
			C = corner_rotate_map[0][type.value]
			swap2(self.cp[C[0]], self.cp[C[2]])
			swap2(self.cp[C[1]], self.cp[C[3]])
			swap2(self.co[C[0]], self.co[C[2]])
			swap2(self.co[C[1]], self.co[C[3]])

			E = edge_rotate_map[0][type.value]
			swap2(self.ep[E[0]], self.ep[E[2]])
			swap2(self.ep[E[1]], self.ep[E[3]])
			swap2(self.eo[E[0]], self.eo[E[2]])
			swap2(self.eo[E[1]], self.eo[E[3]])
		else:
			C = corner_rotate_map[count >> 1][type.value]
			swap(self.cp, C)
			swap(self.co, C)
			if type.value >= 2:
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
			E = edge_rotate_map[count >> 1][type.value]
			if type.value >= 4:
				self.eo[E[0]] ^= 1
				self.eo[E[1]] ^= 1
				self.eo[E[2]] ^= 1
				self.eo[E[3]] ^= 1
			swap(self.ep, E)
			swap(self.eo, E)

	def getBlock(self, level: int, x: int, y: int) -> block_t:
		corner_orient_map = [[1, 3, 4], [1, 5, 3], [1, 2, 5], [1, 4, 2], [0, 4, 3], [0, 3, 5], [0, 5, 2], [0, 2, 4]]
		edge_orient_map = [[4, 3], [5, 3], [5, 2], [4, 2], [0, 3], [0, 5], [0, 2], [0, 4], [1, 3], [1, 5], [1, 2], [1, 4]]
		edge_idd_map = [-1, 8, -1, 11, -1, 9, -1, 10, -1, 0, -1, 1, -1, -1, -1, 3, -1, 2, -1, 4, -1, 7, -1, 5, -1, 6, -1]
		center_idd_map = [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 3, -1, 4, -1, 5, -1, 2, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1]
		nidd = level * 9 + x * 3 + y
		F = [-1, -1, -1, -1, -1, -1]
		if level != 1 and x != 1 and y != 1:
			idd = (level << 1) | x | ((x ^ y) >> 1)
			O = corner_orient_map[idd]
			C = corner_orient_map[self.cp[idd]]
			F[O[0]] = C[self.co[idd]]
			F[O[1]] = C[(1 + self.co[idd]) % 3]
			F[O[2]] = C[(2 + self.co[idd]) % 3]
		elif edge_idd_map[nidd] != -1:
			idd = edge_idd_map[nidd]
			O = edge_orient_map[idd]
			C = edge_orient_map[self.ep[idd]]
			F[O[0]] = C[self.eo[idd]]
			F[O[1]] = C[self.eo[idd] ^ 1]
		elif level != 1 or x != 1 or y != 1:
			F[center_idd_map[nidd]] = center_idd_map[nidd]
		b: block_t = block_t(F)
		return b
'''
cube = cube_t()
print(cube.cp)

print(cube.co)
print(cube.ep)
print(cube.eo)
b = cube.getBlock(0,2,2)
print(b)
cube.rotate(face_type.left,2)
print("rotate top 90")
print(cube.cp)
print(cube.co)
print(cube.ep)
print(cube.eo)
b = cube.getBlock(0,2,2)
print(b)
'''