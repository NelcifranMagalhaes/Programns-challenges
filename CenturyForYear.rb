def centuryFromYear(year)
    
    decimal = year.divmod 100

    if decimal[1] == 0
    	return decimal[0]
    else
    	return decimal[0] +1
    end 
end
print("#century: ",centuryFromYear(2017),"#")