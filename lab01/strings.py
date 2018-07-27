strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for i in strings:
	#sentence.append(i)
	#sentence.append(' ')
	sentence = sentence + i
	sentence = sentence + ' '
print(sentence[:-1])

print(' '.join(strings))
	
