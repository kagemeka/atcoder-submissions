from collections import defaultdict
from bisect import bisect_left


def main():
	s = input()
	n = len(s)
	s = s + s
	t = input()
	if set(t) - set(s):
		print(-1)
		exit()
	d = defaultdict(list)
	for i in range(2 * n):
		d[s[i]] += [i]
	cur = ncnt = 0

	for c in t:
		x = d[c][bisect_left(d[c], cur)]
		if x < n:
			cur = x + 1
		else:
			cur = x - n + 1
			ncnt += 1
	print(ncnt*n + cur)


if __name__ == "__main__":
	main()
