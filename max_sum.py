
def sum_max_gg(deidara):
	max_atual =0
	xtemp = 0
	i = 0
	max_atual = 0
	max_total = -1
	xtemp = 0
	length_list = len(deidara)

	for i in xrange(length_list):
		max_atual = max_atual + deidara[i]

		if max_atual < 0:
			max_atual = 0
			xtemp = i + 1

		if max_atual > max_total :
			max_total = max_atual
			x = xtemp
			y = i
	print x
	print y
	print max_total

def frequently_word_gg(word):

	word_size = len(word)

	cont = 0


	for i in word:
		atual = i


		for j in word:
			if atual is j:
				cont = cont + 1

				maior = j 



def conta_ocorrencias(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias





deidara = [2,-4, 6, 8, -10, 100, -6, 5]
word = "deidaraai"
print conta_ocorrencias(word)
#sum_max_gg(deidara)