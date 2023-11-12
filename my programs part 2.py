import romanNums
import itertools
import gmpy2


# This programm sorts odd numbers in a list, but leaves even numbers in their places

def sort_array(source_array):
	justmylist = source_array
	tempevenlist = []
	for i in justmylist:
		if i%2 == 1:
			tempevenlist.append(i)
			justmylist[justmylist.index(i)] = 1000
	tempevenlist.sort()
	for x in tempevenlist:
		for s in justmylist:
			if s == 1000:
				justmylist[justmylist.index(s)] = x
				break
	return justmylist




sort_array([9,8,7,6,5,4,3,2,1,0])


'''
This programm turns roman numbers into arabic numbers and vice versa, it is on different file
Code is not so good, because i needed to use dictionary, but i already commited to 'if's, that could not turn away ha-ha
'''

print(romanNums.RomanNumerals.to_roman(1234))
print(romanNums.RomanNumerals.from_roman('MMCDXLV'))

# This programm removes certain string part after a certain symbol and strips all trailing whitespaces

def strip_comments(strng, markers):
	for i in markers:
		strng = strng.replace(i,'x')
	strnglist = strng.split('\n')
	newstrnglist = []
	for i in strnglist:
		if 'x' in i:
			k = i.find('x')
			i = i[:k]
			i = i.rstrip()
			newstrnglist.append(i)
		else:
			i = i.rstrip()
			newstrnglist.append(i)

	strng = '\n'.join(newstrnglist)
	return strng


strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

'''
 This programm permutes all combinations of a given string
 I used module for the first time in my programm, should use it more often where i have to, or if i have to,
 instead of trying to make scripts for huuuuge algorithms
'''
def permutations(s):
	perms = [''.join(p) for p in itertools.permutations(s)]
	perms = list(set(perms))
	print(perms)
	

permutations('abcd')

# Just playing a little bit :)

print('2 + 2 = ?')



'''
while True:
	try:
		answer = int(input())
		if answer == 4:
			print('Good job!')
		else:
			print('Bro, wtf?')
		break
	except ValueError:
		print('Bruh.... Just, type a number, ok?')
'''



# Programm for ShipBattles 10x10 , this is not 100% working programm. Has a little bit 'ships crossing' issue
# couldn't find a good algorithm for 'ships crossing' issue


def validate_battlefield(field):

	newfield = []

	for i in field:
		i.reverse()
		newfield.extend(i)

	# Unpacking given list

	unpackedF = []

	for lst in field:
		unpackedF.extend(lst)

	unpackedF = [str(i) for i in unpackedF]

	unpackedF = ''.join(unpackedF)

	# Splitting string with comma

	unpackedF = unpackedF[:10] + ',' + unpackedF[10:]
	unpackedF = unpackedF[:21] + ',' + unpackedF[21:]
	unpackedF = unpackedF[:32] + ',' + unpackedF[32:]
	unpackedF = unpackedF[:43] + ',' + unpackedF[43:]
	unpackedF = unpackedF[:54] + ',' + unpackedF[54:]
	unpackedF = unpackedF[:65] + ',' + unpackedF[65:]
	unpackedF = unpackedF[:76] + ',' + unpackedF[76:]
	unpackedF = unpackedF[:87] + ',' + unpackedF[87:]
	unpackedF = unpackedF[:98] + ',' + unpackedF[98:]

	# counting Battleships for horizontal

	count4 = unpackedF.count('1111')

	unpackedF = unpackedF.replace('1111', '9999')

	# counting Cruisers for horizontal

	count3 = unpackedF.count('111')

	unpackedF = unpackedF.replace('111', '999')

	# counting Destroyers for horizontal

	count2 = unpackedF.count('11')

	unpackedF = unpackedF.replace('11', '99')

	unpackedF = unpackedF.split(',')
	unpackedF = [list(i) for i in unpackedF]

	

	verticalfield = []
	n = 0
	while n < 10:
		for lst in unpackedF:
			verticalfield.append(lst[0 + n])
		n += 1

	verticalfield = ''.join(verticalfield)

	# Splitting string with comma

	verticalfield = verticalfield[:10] + ',' + verticalfield[10:]
	verticalfield = verticalfield[:21] + ',' + verticalfield[21:]
	verticalfield = verticalfield[:32] + ',' + verticalfield[32:]
	verticalfield = verticalfield[:43] + ',' + verticalfield[43:]
	verticalfield = verticalfield[:54] + ',' + verticalfield[54:]
	verticalfield = verticalfield[:65] + ',' + verticalfield[65:]
	verticalfield = verticalfield[:76] + ',' + verticalfield[76:]
	verticalfield = verticalfield[:87] + ',' + verticalfield[87:]
	verticalfield = verticalfield[:98] + ',' + verticalfield[98:]

	tempvertfield = verticalfield
	tempvertfield = tempvertfield.split(',')
	tempvertfield = [list(i) for i in tempvertfield]

	# counting total Battleships

	count4 = count4 + verticalfield.count('1111')

	verticalfield = verticalfield.replace('1111', '9999')

	# counting total Cruisers

	count3 = count3 + verticalfield.count('111')

	verticalfield = verticalfield.replace('111', '999')

	# counting total Destroyers

	count2 = count2 + verticalfield.count('11')

	verticalfield = verticalfield.replace('11', '99')

	# counting total Submarines

	count1 = verticalfield.count('1')
	verticalfield = verticalfield.replace('1', '9')


	diagonal = []
	n = 0
	while n < 10:
		s = 0
		for lst in field:
			if 0 + n + s < 10:
				diagonal.append(lst[0 + n + s])
				s += 1
		n += 1

	diagonal = [str(i) for i in diagonal]

	diagonal = ''.join(diagonal)

	diagonal = diagonal[:10] + ',' + diagonal[10:]
	diagonal = diagonal[:20] + ',' + diagonal[20:]
	diagonal = diagonal[:29] + ',' + diagonal[29:]
	diagonal = diagonal[:37] + ',' + diagonal[37:]
	diagonal = diagonal[:44] + ',' + diagonal[44:]
	diagonal = diagonal[:50] + ',' + diagonal[50:]
	diagonal = diagonal[:55] + ',' + diagonal[55:]
	diagonal = diagonal[:59] + ',' + diagonal[59:]
	diagonal = diagonal[:62] + ',' + diagonal[62:]

	diagonalreverse = []
	n = 0
	while n < 10:
		s = 0
		for lst in tempvertfield:
			if 0 + n + s < 10:
				diagonalreverse.append(lst[0 + n + s])
				s += 1
		n += 1

	diagonalreverse = [str(i) for i in diagonalreverse]

	diagonalreverse = ''.join(diagonalreverse)
	diagonalreverse = diagonalreverse.replace('9','1')

	diagonalreverse = diagonalreverse[:10] + ',' + diagonalreverse[10:]
	diagonalreverse = diagonalreverse[:20] + ',' + diagonalreverse[20:]
	diagonalreverse = diagonalreverse[:29] + ',' + diagonalreverse[29:]
	diagonalreverse = diagonalreverse[:37] + ',' + diagonalreverse[37:]
	diagonalreverse = diagonalreverse[:44] + ',' + diagonalreverse[44:]
	diagonalreverse = diagonalreverse[:50] + ',' + diagonalreverse[50:]
	diagonalreverse = diagonalreverse[:55] + ',' + diagonalreverse[55:]
	diagonalreverse = diagonalreverse[:59] + ',' + diagonalreverse[59:]
	diagonalreverse = diagonalreverse[:62] + ',' + diagonalreverse[62:]



	if '11' in diagonal:
		return False
	elif '111' in diagonal:
		return False
	elif '1111' in diagonal:
		return False

	if '11' in diagonalreverse:
		return False
	elif '111' in diagonalreverse:
		return False
	elif '1111' in diagonalreverse:
		return False


	if count4 != 1:
		return False
	elif count3 != 2:
		return False
	elif count2 != 3:
		return False
	elif count1 != 4:
		return False
	else:
		return True




battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

validate_battlefield(battleField)