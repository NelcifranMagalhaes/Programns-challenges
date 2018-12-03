#Your Informatics teacher at school likes coming up with new ways to help you understand the material. 
#When you started studying numeral systems, he introduced his own numeral system, which he's convinced will help clarify things. 
#His numeral system has base 26, and its digits are represented by English capital letters - A for 0, B for 1, and so on.
#The teacher assigned you the following numeral system exercise: given a one-digit number, 
#you should find all unordered pairs of one-digit numbers whose values add up to the number.
import string

def newNumeralSystem(number):
	listAlphabet = list(string.ascii_uppercase)
	listOfLetters = []
	number_int = listAlphabet.index(number)
	for x in range(len(listAlphabet)):
		for y in range(len(listAlphabet)):
			if x + y == number_int:
				sentence = "%s + %s" %(listAlphabet[x],listAlphabet[y])
				inverseSentence = "%s + %s" %(listAlphabet[y],listAlphabet[x])
				if inverseSentence not in listOfLetters:
					listOfLetters.append(sentence)

	print (listOfLetters)
newNumeralSystem('G') #testing