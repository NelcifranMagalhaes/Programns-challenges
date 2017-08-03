def centuryFromYear(year)
    
    decimal = year.divmod 100

    if decimal[1] == 0
    	return decimal[0]
    else
    	return decimal[0] +1
    end 
end

def max_sum(list_of_numbers)
    x =0
    big_sum=0

    big_i =0
    big_j = 0
    i =0


    length_list = list_of_numbers.size


    while x < length_list
        j=i+1
        while j< length_list

            sum_gg = 0
            k=i
            puts "primeiro while"
            
            while k <= j

                sum_gg = sum_gg + list_of_numbers[k]

                k+=1
            end

            if sum_gg > big_sum

                big_i = i
                big_j = j
                big_sum = sum_gg
                
            end


            j+=1
            
        end
        i+=1
    end
    puts #{big_i} "e" #{big_j} "=" #{big_sum}  

end

deidara = [2, -4, 6, 8, -10, 100, -6, 5]

max_sum(deidara)