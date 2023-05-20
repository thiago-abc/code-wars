"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. 
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
	s = s.lower()
	count_o = 0
	count_x = 0
	for n in s:
		if n == 'o':
			count_o += 1
		elif n == 'x':
			count_x += 1
		else:
			pass;
	return True if count_o == count_x else False

