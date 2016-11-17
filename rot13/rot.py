def rot(word):
	num_val = {"a": 0, "b": 1, "c": 2, "d":3, "e":4, "f": 5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, \
			"p": 15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
	rot = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
	is_upp = False
	build = []
	for l in word:
		if l.isupper():
			l = l.lower()
			is_upp = True
		try:
			l = rot[(num_val[l] + 13) % (len(rot))]
			build.append(l)
		except:
			build.append(l)
	if is_upp:
		build[0] = build[0].upper()
	return "".join(build)

print rot("Hello")