__author__ = "Saad Khan"

from pathlib import Path

import numpy as np
def wordtodoc():
    with Path('test.tags').open() as f:
 	i = 0   
	for line in f:
		i= i+1
		if line =='\n':
			print(i)

if __name__ == '__main__':
    # Load vocab file
    wordtodoc()
