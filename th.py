import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import os
np.set_printoptions(threshold=np.inf)

def writeWords(filename,X1_sentence):	
	with open(filename,'w') as f:
            sent = []
            words = ''
	    for sentence in X1_sentence:
		frame = np.asarray(sentence)
		i = 0 
		for word in frame:	
                        #words+=(word[2]+' ')
			if(i+1==len(frame)):
				f.write(word[16])
			else:
				print(word[16])
				f.write(word[16]+' ')
			i=i+1
		#sent.append(words+'\n')
                f.write('\n')
                #words = ''
            #f.write(sent)



def writeTags(filename,Y1_sentence):	
	with open(filename,'w') as f:
	    for sentence in Y1_sentence:
			i = 0 
			for tag in sentence:
				if(i+1==len(sentence)):
					f.write(tag)
				else:
					f.write(tag+' ')
				i=i+1
			f.write('\n')





def writeFeatureVector(X1_sentence,file_name):
    all_data = []
    #features = np.load('addFeatures.npy')
    for sentence in X1_sentence:
        sentence = sentence.drop([88], axis=1)
        feat_vec = []
    	words = ''
    	frame = np.asarray(sentence)
    	for word in frame:
		i=0
		for part in word:
			if(isinstance(part, str)):
				word[i] = int(part,2)		
			i=i+1        	
		word[word == True]=1
        	word[word == False]=0
		#print(word)
        	feat_vec.append(word)
        all_data.append(feat_vec)
    #print(file_name)
    np.save('/home/saad/ritter_4',all_data)

def writecsv(file_name,X1_sentence):
	if 'sentenceFiles' in file_name:
		file_name.replace("sentenceFiles","csvfiles/simple/")
		print(file_name)
	else:
		file_name.replace('sentenceFiles','csvfiles/ids/')	
	df = pd.concat(X1_sentence)
	df.to_csv(file_name+'.csv')

path = '/home/saad/All_Config_Files/ritter_train_10/ids'
#filename = '/home/saad/Downloads/_ritter.train_configs/_ritter.train_config_4.sentence.pkl'

#for fname in os.listdir(path):
#filename = os.path.join(path,fname)
with open('/home/saad/All_Config_Files/ritter_train_4/ids/_ritter.train_config_4.sentence.idx.pkl', 'r') as input:
	file_name, f_key, X1_sentence, Y1_sentence = pickle.load(input)
     	# just PLO
	#print(X1_sentence[2])
	#for y in X1_sentence[3].columns:
		#if(X1_sentence[3][y].dtype == object):
			#print(X1_sentence[3][y])
		#else:
			#print(X1_sentence[3][y])
	
	#writecsv(filename,X1_sentence)
	temp = [['O' if item == 'MISC' else item for item in lst] for lst in Y1_sentence]
	Y1_sentence = temp
	#filename = filename.replace(".sentence.idx.pkl","")
	#print(filename)
	#fname = fname.replace(".sentence.idx.pkl","_features")	    	
	#print('writing words')
    	#writeWords(file_name+'.words',X1_sentence)
    	#print('writing tags')
    	#writeTags(file_name+'.tags',Y1_sentence)
	writeFeatureVector(X1_sentence,'')
	 
	

