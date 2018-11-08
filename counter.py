from collections import Counter
with open('/home/saad/tf_ner/data/example/wnut15/train') as f:
    ln = f.readlines()
    non_blank_count = 0
    count = []
    for line in ln:
        if line == '\n':
            non_blank_count += 1
	else:
            l = line.split('\t')
            l[1] = l[1].rstrip()
            l[1] = l[1].split('-', 1)[-1:]
            count.append(l[1][0])
    print(Counter(count))


print('no. of sentences : ' ,non_blank_count)



