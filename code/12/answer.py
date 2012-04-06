def factor(n):
	start = 2
	ret = dict()
	while n > 1:
		if n % start == 0:
			n = n / start
			try:
				ret[start] = ret[start] + 1
			except KeyError:
				ret[start] = 1
		else:
			start = start + 1
	return ret

def countDivisors(n):
	factors = factor(n)
	ret = 1
	for f in factors.keys():
		ret = ret * (factors[f] + 1)
	return ret

def calcTriangleNumber(n):
	return n * (n + 1) / 2

n = 1
while True:
	triangleNumber = calcTriangleNumber(n)
	if countDivisors(triangleNumber) > 500:
		print triangleNumber
		break
	n = n + 1
