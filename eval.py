from __future__ import print_function
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
import fileinput
import sys
import os
from collections import defaultdict, namedtuple

path = '/home/saad/resultsincFeats/'
labels = ['LOC','ORG','PER']
'''
with open('bnchmarking.txt', 'w') as f:
	f.write('Cross-Validation\t'+'Config\t'+'Label\t'+'Precision\t'+'Recall\t'+'f1\t'+'Algo\t'+'datasetTrain\t'+'datasetValidation\n')
	for fname in os.listdir(path):
		#filename = os.path.join(path,fname)
		print(fname)
		filename=''
		y_true = []
		y_pred = []
		with open(path+fname, 'rb') as input:
			for line in input:
				if(len(line)>1):	
					k = line.split(' ')
					y_true.append(k[1])
					y_pred.append(k[2].rstrip())
			P, R, F, S =  precision_recall_fscore_support(y_true, y_pred,labels=labels)

			for k in range(len(P)):		
				f.write('0'+'\t'+fname[-2:]+'\t'+labels[k]+'\t'+str(round(P[k],4))+'\t'+str(round(R[k],4))+'\t'+str(round(F[k],4))+'\t'+'Bi-charsLstm'+'\t'+fname[2:4]+'Wnut_train'+'\t'+fname[-5:-3]+'Wnut_test'+'\n')



			P_avg, R_avg, F_avg, S_avg = precision_recall_fscore_support(y_true, y_pred,labels=labels,                           average='weighted')
			f.write('0'+'\t'+fname[-2:]+'\t'+'average'+'\t'+str(round(P_avg,4))+'\t'+str(round(R_avg,4))+'\t'+str(round(F_avg,4))+'\t'+'Bi-charsLstm'+'\t'+fname[2:4]+'Wnut_train'+'\t'+fname[-5:-3]+'Wnut_test'+'\n\n\n')
'''




y_true = []
y_pred = []
with open('/home/saad/w16ResultsIncFeats/test15/feat_4/tr16test15.04.txt', 'rb') as input:
	for line in input:
		if(len(line)>1):	
			k = line.split(' ')
			y_true.append(k[1])
			y_pred.append(k[2].rstrip())
	P, R, F, S =  precision_recall_fscore_support(y_true, y_pred,labels=labels)

	for k in range(len(P)):		
		print(F[k])

P_avg, R_avg, F_avg, S_avg = precision_recall_fscore_support(y_true, y_pred,labels=labels,                           average='weighted')

print('avg',F_avg)
