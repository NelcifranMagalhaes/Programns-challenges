file = File.open("Caminho do arquivo", "rb")

contents = file.read
contents.gsub!(/\r\n?/, "\n")
lista_cheia = []

contents.each_line do |line|
  #lista = line.split(/\t+/)
  lista_cheia.push(line.split(/\t+/)) #percorre as linhas e tira os tabs
end
lista_cheia.delete_at(0) #deletei a primeira linha do arquivo que tem os campos(Comprador,descrição,Preço Uniário,Quantidade,Endereço,Fornecedor)
count = 0
lista_pra_inserir = []
lista_cheia.each do |ls|
	lista_individual = []
  	for i in 0..lista_cheia.size+1
		lista_individual.push(ls[i])
  	end
  	lista_pra_inserir.push(lista_individual)
	count = count +1
end
lista_pra_inserir.each do |novo|
	
	puts "relatorie.create(buyer: #{novo[0]},description: #{novo[1]},price: #{novo[2]},quantity: #{novo[3]},address: #{novo[4]},owner: #{novo[5]}) "
end 

