
def listtoset(filename):
	with open(filename, 'rb') as input:
		wnut = []
		for line in input:
			if(line!='\n' ):
				t = line.split('\t')
				if(t[1].rstrip()!='O' and len(t[0])>0):
					t[1] = t[1].rstrip().split('-',1)[1].lower()
					if(t[1]=='location'):
						t[1] = 'geo-loc'
					elif(t[1]=='corporation'):					
						t[1] = 'company'
					word = t[0].lower()+'_'+t[1]
					wnut.append(word)
	#print(len(wnut),filename)	
	return set(wnut) 
#15sets
trainset15 = listtoset('/home/saad/datasets/wnut15/dropbox/train')
devset15 = listtoset('/home/saad/datasets/wnut15/dropbox/dev')

#ritter
ritterset = listtoset('ritter.txt')

#16 sets
trainset16 = listtoset('/home/saad/datasets/wnut16/train')
devset16 = listtoset('/home/saad/datasets/wnut16/dev')
testset16 = listtoset('/home/saad/datasets/wnut16/test')

#17 sets
trainset17 = listtoset('/home/saad/datasets/wnut17/train')
devset17 = listtoset('/home/saad/datasets/wnut17/dev')
testset17 = listtoset('/home/saad/datasets/wnut17/test')


print(len(trainset15),len(ritterset),len(testset16))
print(len(devset15),len(devset16))

print('trainset15')
print('Intersection trainset15,15dev', len(trainset15.intersection(devset15)))
print('Intersection trainset15,Ritter', len(trainset15.intersection(ritterset)))
print('Intersection trainset15,16train', len(trainset15.intersection(trainset16)))
print('Intersection trainset15,16dev', len(trainset15.intersection(devset16)))
print('Intersection trainset15,16test', len(trainset15.intersection(testset16)))
print('Intersection trainset15,17train', len(trainset15.intersection(trainset17)))
print('Intersection trainset15,17dev', len(trainset15.intersection(devset17)))
print('Intersection trainset15,17test', len(trainset15.intersection(testset17)))
print('\n')
print('devset15')
print('Intersection devset15,Ritter', len(devset15.intersection(ritterset)))
print('Intersection devset15,16train', len(devset15.intersection(trainset16)))
print('Intersection devset15,16dev', len(devset15.intersection(devset16)))
print('Intersection devset15,16test', len(devset15.intersection(testset16)))
print('Intersection devset15,17train', len(devset15.intersection(trainset17)))
print('Intersection devset15,17dev', len(devset15.intersection(devset17)))
print('Intersection devset15,17test', len(devset15.intersection(testset17)))
print('\n')
print('ritter')
print('Intersection train16,Ritter', len(trainset16.intersection(ritterset)))
print('Intersection dev16,Ritter',len(devset16.intersection(ritterset)))
print('Intersection test16,Ritter',len(testset16.intersection(ritterset)))
print('Intersection train17,Ritter', len(trainset17.intersection(ritterset)))
print('Intersection dev17,Ritter ',len(devset17.intersection(ritterset)))
print('Intersection test17,Ritter ',len(testset17.intersection(ritterset)))
print('\n')
print('trainset16')
print('Intersection dev16,16train',len(devset16.intersection(trainset16)))
print('Intersection test16,16train',len(testset16.intersection(trainset16)))
print('Intersection train17,16train', len(trainset17.intersection(trainset16)))
print('Intersection dev17,16train',len(devset17.intersection(trainset16)))
print('Intersection test17,16train',len(testset17.intersection(trainset16)))
print('\n')
print('devset16')
print('Intersection test16,16dev',len(testset16.intersection(devset16)))
print('Intersection train17,16dev', len(trainset17.intersection(devset16)))
print('Intersection dev17,16dev',len(devset17.intersection(devset16)))
print('Intersection test17,16dev',len(testset17.intersection(devset16)))
print('\n')
print('test16')
print('Intersection train17,16test', len(trainset17.intersection(testset16)))
print('Intersection dev17,16test',len(devset17.intersection(testset16)))
print('Intersection test17,16test',len(testset17.intersection(testset16)))
print('\n')
print('traintset17')
print('Intersection test17,17train', len(testset17.intersection(trainset17)))
print('Intersection dev17,17train',len(devset17.intersection(trainset17)))
print('\n')
print('devset17')
print('Intersection test17,17dev', len(testset17.intersection(devset17)))
print('\n')
print('testset17')

'''
print(list(trainset15.intersection(devset17))[0:50])
print('\n')
print(list(trainset15)[0:50])
print(list(testset16)[0:50])
print('\n')
print(list(ritterset)[0:50])
print('\n')
print(list(trainset17)[0:50])
'''
