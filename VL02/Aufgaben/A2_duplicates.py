import numpy as np
from collections import defaultdict

# sorting is optional parameter, default true'
def find_duplicates(set, sort=true):
	_set = defaultdict(int)
	for number in set:
		_set[number] += 1
		# Print if found a duplicate!
		# if number in set:
			# print("Found a duplicate, its " + str(number) + "!")

	if sort:
		sorted_set = sorted(_set.items())
	
	# Print numbers which are more often found than 1 time!
	for i, j in sorted_set:
		if j > 1:
			print("%d was found %d times!" % (i, j))
			


if __name__ == "__main__":
	# Generater some random numbers with gaussian algorithm
	np.random.seed(1)
	x = np.random.randint(100, size=50)

	# find the duplicates!
	find_duplicates(x)

	print("frequen< in O- notation:")
	print("O(n) = n")