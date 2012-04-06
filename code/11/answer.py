class Matrix(object):
	def __init__(self, data):
		self.data = data

	def maxHorizontalProduct(self):
		ret = 0
		for i in range(0, len(self.data)):
			for j in range(0, len(self.data[i]) - 3):
				product = reduce((lambda a, b: a * b), [self.data[i][j + k] for k in range(0, 4)], 1)
				ret = max(ret, product)
		return ret

	def maxVerticalProduct(self):
		ret = 0
		for i in range(0, len(self.data) - 3):
			for j in range(0, len(self.data[i])):
				product = reduce((lambda a, b: a * b), [self.data[i + k][j] for k in range(0, 4)], 1)
				ret = max(ret, product)
		return ret
	
	def maxDiagonalRightProduct(self):
		ret = 0
		for i in range(0, len(self.data) - 3):
			for j in range(0, len(self.data[i]) - 3):
				product = reduce((lambda a, b: a * b), [self.data[i + k][j + k] for k in range(0, 4)], 1)
				ret = max(ret, product)
		return ret

	def maxDiagonalLeftProduct(self):
		ret = 0
		for i in range(0, len(self.data) - 3):
			for j in range(3, len(self.data[i])):
				product = reduce((lambda a, b: a * b), [self.data[i + k][j - k] for k in range(0, 4)], 1)
				ret = max(ret, product)
		return ret

if __name__ == '__main__':
	f = open('input.txt', 'r')
	lines = f.readlines()
	input_data = list()
	for line in lines:
		input_data.append(map(int, line.strip().split(' ')))

	m = Matrix(input_data)
	#print m.maxVerticalProduct()
	max(m.maxHorizontalProduct(), m.maxVerticalProduct(), m.maxDiagonalRightProduct(), m.maxDiagonalLeftProduct())
