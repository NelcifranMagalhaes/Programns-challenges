
#Given an array a that contains only numbers in the range from 1 to a.length, 
#find the first duplicate number for which the second occurrence has the minimal index.
#In other words, if there are more than 1 duplicated numbers, 
#return the number for which the second occurrence has
#a smaller index than the second occurrence of the other number does. 
#If there are no such elements, return -1.
#A function that mount a dictionary with duplicated numbers of a list

def dictionaryMount(a):
	index_first = 0
	dict_numbers = {}
	salved = 0

	for index,x in enumerate(a):
		salved = x
		lista_of_index = []

		for index2,y in enumerate(a):
			if salved == y:
				lista_of_index.append(index2)

		dict_numbers[x] = lista_of_index

	return dict_numbers


def firstDuplicate(a):
	dict_final = {} #a dictionary with just duplicated numbers
	big = 0
	list_of_bigers = {} #a dictionary with just big indices of duplicated numbers 
	dict_numbers = dictionaryMount(a) #a dictionary of function

	for k,v in dict_numbers.iteritems():
		if len(v) >= 2:
			
			dict_final[k] = v
			if len(dict_final[k]) > 2:
				 
				dict_final[k].pop() #deleting if lenght of list > 2
	
	#if dict just has a duplicated number
	if len(dict_final) == 1 :
		number_extract = dict_final.keys()

		return number_extract[0] #number extracted of list,that has just one number

	#if dict has more that 2 duplicated numbers
	elif len(dict_final) >= 2 :
		
		for k,v in dict_final.iteritems():
				
			list_of_bigers[k] = max(v)
		
		small = min(list_of_bigers.values()) #min value of indices

		for x, y in list_of_bigers.iteritems():
			if y == small:
				return x
				
	else:

		return -1


a = [2, 3, 3, 1, 5, 2]
b = [2, 4, 3, 5, 1]
c = [2, 4, 3, 5, 4]
d = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
e = [1, 1, 2, 2, 1]

print firstDuplicate(e)