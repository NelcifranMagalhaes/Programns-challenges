#He wants to arrange them from smallest to largest so that each statue will be bigger than the 
#previous one exactly by 1. He may need some additional statues to be able to accomplish that. 
#Help him figure out the minimum number 
#of additional statues needed.
#For statues = [6, 2, 3, 8], the output should be
#makeArrayConsecutive2(statues) = 3.
#Ratiorg needs statues of sizes 4, 5 and 7.

def makeArrayConsecutive2(statues):
	statues.sort() #sorting a list
	max_value = max(statues)
	# min_value = min(statues)
	count = 0
	print statues
	for x in statues:

		if (x+1) not in statues and x != max_value:

			count +=1
			statues.append(x+1)
			statues.sort()
	return count


a = [6, 2, 3, 8]
b = [0, 3]
c = [1]


print makeArrayConsecutive2(c)
