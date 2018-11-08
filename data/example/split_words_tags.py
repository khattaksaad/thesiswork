__author__ = "Saad Khan"

from pathlib import Path

import numpy as np

def senttodoc():
    file_path = 'wnut17/'
    for n in ['train','dev','test']:
        words = []
        tags = []
        sents = []
        sent = ''
        sent_tags = ''
        with Path(file_path + n).open() as f:
    	    for line in f:
    	        	ls = line.split('\t')
                	word, tag = ls[0], ls[-1]
			print(word+'ss')
                	if word == '\n' or word=='':
				print('if ',word)
                    		sents.append(sent)
		            	tags.append(sent_tags)
				sent = ''
				sent_tags = ''
			else:
			    print('else ',word)
		            if sent != '':
		                sent = sent + ' ' + word
		                sent_tags = sent_tags + ' ' + tag.rstrip()
		            else:
		                sent += word
		                sent_tags += tag.rstrip()
        with Path(file_path+n+'.words').open('w') as f:
            for sent in sents:
                f.write(sent + '\n')
        with Path(file_path + n + '.tags').open('w') as f:
            for tag in tags:
                f.write(tag + '\n')

def wordtodoc():
    file_path = '/home/saad/tf_ner/data/example/'
    for n in ['train','dev','test']:
        words = []
        tags = []
        with Path(file_path+n).open() as f:
                for line in f:
                    ls = line.split(' ')
                    word, tag = ls[0],ls[-1]
                    words.append(word)
                    tags.append(tag.rstrip())
        with Path(file_path+n+'.words').open('w') as f:
            for word in words:
                word = word.strip()
                if word == '\n':
                    f.write('')
                else:
                    f.write(word+'\n')
        with Path(file_path + n + '.tags').open('w') as f:
            for tag in tags:
                if tag == '':
                    f.write('')
                else:
                    f.write(tag + '\n')

if __name__ == '__main__':
    # Load vocab file
    senttodoc()
