class Mat

def verprimo(num)

	num = num.to_i
	
	if (num < 2)
		puts "numero deve ser maior que 1"
		exit
	end
	
   raiz = Math.sqrt(num)
   raiz = raiz.to_i + 1
   ret = true

   
   for ct in (2..raiz)
      if (num % ct == 0 && num != ct)
        ret = false
        break
      end
   end
   
   return ret
end


def fatores(num)

  num = num.to_i

  array_divisiveis = Array.new([]) 

  for x in 2..num
    if num % x == 0
      array_divisiveis.push(x) 

    end

  end

  array_primos = Array.new([])

  for d in array_divisiveis

    if self.verprimo(d) == true

      array_primos.push(d) 

    end

  end


  return array_primos

end


def fatores_do_mmc(num,array_primos)
  
  array_primos.sort
  

end



end



@vamo = Mat.new

x = @vamo.fatores(100)

puts x