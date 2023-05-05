"""You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0."""

def positive_sum(arr):
	positive = 0
	for a in arr:
		if a > 0:
			positive += a
		else:
			pass
	return positive
