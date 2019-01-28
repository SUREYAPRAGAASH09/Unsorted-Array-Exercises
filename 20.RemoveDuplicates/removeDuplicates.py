def built_dictionary(array): # To Built a dictionary  
    d = {} #creating a empty dictionary 
    count = 0 
    for i in array: 
        count = 1 
        if i in d: 
            d[i] = d[i] + 1 
        else: 
            d[i] = count  
    return list(d.keys())

array = [7,2,0,1,5,7,9,1,8]
print(built_dictionary(array)) 
