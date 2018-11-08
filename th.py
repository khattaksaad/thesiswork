import pickle
import pandas as pd
import numpy as np
from pathlib import Path
np.set_printoptions(threshold=np.inf)
all_data = []
features = np.load('addFeatures.npy')
for i in features:
    print i
    print "break"
#with open('_ritter.train_config_1.sentence.pkl', 'rb') as input:
#    file_name, f_key, X1_sentence, Y1_sentence = pickle.load(input)
#    # just PLO
#    temp = [['O' if item == 'MISC' else item for item in lst] for lst in Y1_sentence]
#    Y1_sentence = temp
#    for sentence in X1_sentence:
#			#print (item)
#                        feat_vec = []
#			frame = np.asarray(sentence)
#			for word in frame:
#				new = word[3:]
#				new[new == True]=1
#				new[new == False]=0
#				feat_vec.append(new)
#     			all_data.append(feat_vec)
#    np.save('addFeatures',all_data)

				

			
