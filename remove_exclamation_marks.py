#Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

import re

def remove_exclamation_marks(s):
	return re.sub(r'!', '', s)

print(remove_exclamation_marks('Hello World!!!!!!!!!!'))
