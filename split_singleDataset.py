from sklearn.model_selection import train_test_split
import numpy as np
from pathlib import Path


ds_test_size = 0.20
r = [42, 19, 10]
dit = '/home/saad/miscfiles/'
X1_token = []
Y1_token = []
files = ['ritter_train_words.txt','ritter_train_tags.txt']

for filename in files:
	with open(filename, 'rb') as input:
		for line in input:	
			if(line!='\n' and filename =='ritter_train_words.txt' ):
				X1_token.append(line)
			elif(line!='\n' and filename =='ritter_train_tags.txt'):
				Y1_token.append(line)
				

print(len(Y1_token),len(X1_token))

feat_vectors = np.load('/home/saad/All_Config_Files/ritter.train.41/features/_ritter.train_config_41_features.npy')

for d in range(len(r)):
	Xtr, Xte, ytr, yte = train_test_split(X1_token, Y1_token, test_size=ds_test_size,
	                                                                  random_state=r[d])
	XFtr, XFte, ytr, yte = train_test_split(feat_vectors, Y1_token, test_size=ds_test_size,
	                                                                  random_state=r[d])
	print(ytr[10:20])
        #np.save('ritter_train_features_config41_'+str(d),XFtr)
	#np.save('ritter_dev_features_config41_'+str(d),XFte)
	print(ytr[10:20])

'''	
	with open(dit+'ritter_train_words_'+str(d),'w') as w,open(dit+'ritter_train_tags_'+str(d),'w') as t:
		for sents,tags in zip(Xtr,ytr):
			w.write(sents.decode("utf-8"))
			t.write(tags.decode("utf-8"))
	with open(dit+'ritter_dev_words_'+str(d),'w') as w,open(dit+'ritter_dev_tags_'+str(d),'w') as t:
			for sents,tags in zip(Xte,yte):
				w.write(sents.decode("utf-8"))
				t.write(tags.decode("utf-8"))
'''
#print(len(feat_vectors[0]))
