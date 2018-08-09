def list_of_text(tex, wid):
	count = 0 #count of slice 
	count_of_xd = 1 #count of lines
	list_of_snake =[] #list that contains elements of text transformed in lists
	size_of_tex = len(tex)
	
	while count <= size_of_tex:

		slice = tex[count:count+wid] #slicing the list

		if count_of_xd % 2 == 0: #if lines is pair reverse that list
			slice = slice[::-1] 
		
		list_of_snake.append(list(slice))
		count_of_xd = count_of_xd +1
		count = count + wid

	return list_of_snake


def charLocation(tex, wid, ch):

	list_of_find = []
	list_tex = list_of_text(tex,wid)
	for index,x in enumerate(list_tex):
		if ch in x:
			for index_2,y in enumerate(x):
				if ch == x[index_2]:
					list_of_find.append([index,index_2])

	return list_of_find






text = "For there was never yet philosopher that could endure the toothache patiently. -- William Shakespeare, Much Ado About Nothing"
wid = 17
ch = "t"


print charLocation(text,wid,ch)

