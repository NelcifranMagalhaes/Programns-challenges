#Dado um conjunto de números, descobrir o subconjunto em que a soma
#dos elementos são de máxima soma.
def sum_max_gg(deidara):
	max_atual =0
	xtemp = 0
	i = 0
	max_atual = 0
	max_total = -1
	xtemp = 0
	length_list = len(deidara)

	for i in range(length_list):
		max_atual = max_atual + deidara[i]

		if max_atual < 0:
			max_atual = 0
			xtemp = i + 1

		if max_atual > max_total :
			max_total = max_atual
			x = xtemp
			y = i
	print(x)
	print(y)
	print(max_total)

# Dada uma palavra, escreva um algoritmo que retorne a sequência de
#caracteres que mais aparecem em sequência.
def frequently_word_gg(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias





deidara = [2,-4, 6, 8, -10, 100, -6, 5]
sum_max_gg(deidara)

word = "deidaraai"
print (frequently_word_gg(word))
