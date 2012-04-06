class TriangleMatrix(object):
	def __init__(self):
		self.data = dict()
	
	def get_value(self, x, y):
		try:
			return self.data[x][y]
		except:
			return 0
	
	def set_value(self, x, y, value):
		try:
			self.data[x][y] = value
		except:
			self.data[x] = dict()
			self.data[x][y] = value

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

lines = map(str.strip, lines)
data = list()

for line in lines:
	data.append(map(int, line.split(' ')))

m = TriangleMatrix()
for i in range(len(data), 0, -1):
	for j in range(0, i):
		if i == len(data):
			m.set_value(i - 1, j, data[i - 1][j])
		else:
			m.set_value(i - 1, j, max(m.get_value(i, j), m.get_value(i, j + 1)) + data[i - 1][j])

print m.get_value(0, 0)
