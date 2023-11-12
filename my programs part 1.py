import romanNums
import itertools
import gmpy2



# This is random python file, just to configure my Sublime Text

# My first ever programm on python, i'm proud 

dota2 = "Let's go Dota"

print(dota2)

# Homework from thenewboston youtube channel

for x in range(0, 101, 4):
	print(x)

# Temporary programms for codewars.com

# This programm returns True if a number exits square root with integer number
def is_square(n): 
	if n < 0:
		return False
	else:
		mysquare = int(n**0.5)
		mynumber = mysquare**2
		if mynumber == n or mynumber == 0:
			return True
		else:
			return False

print(is_square(3))


# This programm returns element which occurs odd number of times in number lists

def find_it(seq):
	for i in seq:
		mycount = seq.count(i)
		expnum = int(mycount / 2)
		expnum2 = expnum * 2
		if expnum2 != mycount:
			return i
			break

# Not my code, my disgrace and failure

def find_outlier(integers):
	odds = [x for x in integers if x%2!=0]
	evens = [x for x in integers if x%2==0]
	return odds[0] if len(odds)<len(evens) else evens[0]

randomlist = [11,13,19,21,6]

print(find_outlier(randomlist))

# Programm which do some stuff

def to_camel_case(text):
	if text == "":
		return
	my = text.replace('-',' ').replace('_',' ')
	big = my[0].isupper()
	print(big)
	if big is True:
		myup = my.title().replace(' ','')
		print(myup)
	else:
		myup = my.title().replace(' ','')
		print(text[0]+myup[1:])
    

to_camel_case('the-new-market')

# This programm concatenates every single digit of a number as strings

def square_digits(num):
    goodnum = num
    numIntoString = [int(d) for d in str(num)]
    numIntoSquare = [str(i**2) for i in numIntoString]
    unpackednum = int(''.join(numIntoSquare))
    print(unpackednum)


square_digits(1234)

# This programm i assigned a value of loop result to a variable outside of the loop
# This programm counts people in a bus

def number(bus_stops):
    currentpeople = 0
    for i in bus_stops:
    	currentpeople = currentpeople + i[0]
    	currentpeople = currentpeople - i[1]
    return currentpeople


buslist = [[15,0],[4,6],[7,2]]

number(buslist)

# This programm takes all zeros from a list and appends them all in the end of a list

def move_zeros(lst):
	for x in lst:
		if x == 0:
			lst.remove(x)
			lst.append(x)
	return(lst)

biglist = ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])

move_zeros(biglist)

# This programm finds substrings in a string list

def in_array(array1, array2):
    newstringmix = []
    stringedarray2 = ' '.join(array2)
    for s in array1:
    	checking = stringedarray2.find(s)
    	if checking >= 0 and s not in newstringmix:
    		newstringmix.append(s)
    newstringmix.sort()
    return newstringmix
    	



stringmix1 = ["live", "arp", "strong"]
stringmix2 = ["lively", "alive", "harp", "sharp", "armstrong"]

in_array(stringmix1, stringmix2)

# This programm makes tribonacci expressions

def tribonacci(signature, n):
	if n <= 3:
		newresult = []
		o = 0
		while n > 0:
			newresult.append(signature[o])
			n = n - 1
			o = o + 1
		return newresult
	else:
		limit = n - 3
		i = 0
		tribonacciList = signature
		while limit > 0:
			tribonacciList.append(sum(tribonacciList[i:]))
			limit = limit - 1
			i = i + 1
		return tribonacciList

tribonacci([1,1,1], 10)

# This programm finds an index of a list which have equal sums on left side and right side of itself
# I could get indexes with range(len(list)) scheme, i need to remember that technique, and add to my arsenal

def find_even_index(arr):
    mygoodlist = arr
    mygoodlistindexes = []
    templist = mygoodlist.copy()
    finalindex = -1
    for n in templist:
    	mygoodlistindexes.append(templist.index(n))
    	templist[templist.index(n)] = None
    for i in mygoodlistindexes:
    	m = i + 1
    	if sum(mygoodlist[m:]) == sum(mygoodlist[:i]):
    		finalindex = i
    		break
    return finalindex

find_even_index([0,0,0,0,0])

totallist = [1,2,3,4,5,6,10,20]
tempvar = range(len(totallist))
print(tempvar)


# This programm is a fixed digits calculator, maybe i could do better, but programm works


def zero(f = None): 
	if f == None:
		return 0
	else:
		pl = 0
		f = eval(f)
		return int(f)
def one(f = None): 
	if f == None:
		return 1
	else:
		pl = 1
		f = eval(f)
		return int(f)
def two(f = None): 
	if f == None:
		return 2
	else:
		pl = 2
		f = eval(f)
		return int(f)
def three(f = None):
	if f == None:
		return 3
	else:
		pl = 3
		f = eval(f)
		return int(f)
def four(f = None): 
	if f == None:
		return 4
	else:
		pl = 4
		f = eval(f)
		return int(f)
def five(f = None): 
	if f == None:
		return 5
	else:
		pl = 5
		f = eval(f)
		return int(f)
def six(f = None): 
	if f == None:
		return 6
	else:
		pl = 6
		f = eval(f)
		return int(f)
def seven(f = None): 
	if f == None:
		return 7
	else:
		pl = 7
		f = eval(f)
		return int(f)
def eight(f = None): 
	if f == None:
		return 8
	else:
		pl = 8
		f = eval(f)
		return int(f)
def nine(f = None):
	if f == None:
		return 9
	else:
		pl = 9
		f = eval(f)
		return int(f)

def plus(n):
	pl = 'pl'
	return f'{pl} + {n}'
def minus(n):
	pl = 'pl'
	return f'{pl} - {n}'
def times(n):
	pl = 'pl'
	return f'{pl} * {n}'
def divided_by(n): 
	pl = 'pl'
	return f'{pl} / {n}'

eight(divided_by(three()))


# This programm retrieves count of 1-s in binary form of a given digit

def count_bits(n):
	x = n
	x = bin(x)
	x = str(x)
	totalones = []
	for i in x:
		if i == "1":
			totalones.append(1)
	return len(totalones)

count_bits(5555)

# This programm works like Facebooks liking message system

def likes(names):
    if len(names) == 0:
    	return 'no one likes this'
    elif len(names) == 1:
    	return f'{names[0]} likes this'
    elif len(names) == 2:
    	return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
    	return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
    	return f'{names[0]}, {names[1]} and {len(names[2:])} others like this'

likes(['Max','John','Mark'])