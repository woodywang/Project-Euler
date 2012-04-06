power_set = set()

for a in range(2, 101):
	for b in range(2, 101):
		power_set.add(a ** b)

print len(power_set)
