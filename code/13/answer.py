f = open('input.txt', 'r')
lines = f.readlines()

s = 0
for line in lines:
	s = s + long(line.strip())

result = str(s)
print result[:10]
