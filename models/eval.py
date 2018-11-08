from __future__ import print_function
from sklearn.metrics import precision_recall_fscore_support
import fileinput
import sys
from collections import defaultdict, namedtuple

y_true = []
y_pred = []
for line in fileinput.input():
	if(len(line)>1):	
		k = line.split(' ')
		y_true.append(k[1])
		y_pred.append(k[2].rstrip())
k = precision_recall_fscore_support(y_true, y_pred, average='macro',labels=['LOC', 'PER', 'ORG','O'])
print(k)
