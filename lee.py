xs = [1440,1760,1260,1460,1800]
dd = [240,560,60,260,600]
t = 4
for o in range(5):
	for i in range(5):
		xs.append(xs[t]+dd[i])
	xs.append('        ')

print(xs)