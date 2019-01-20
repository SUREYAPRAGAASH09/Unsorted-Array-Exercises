def built_dictionary(array): # To Built a dictionary  
    dictionary = {} #creating a empty dictionary 
    count = 0 
    for i in array: 
        count = 1 
        if i in dictionary: 
            dictionary[i] = dictionary[i] + 1 
        else: 
            dictionary[i] = count  
    return dictionary

def find_key_from_dictionary(dictionary,max_element): # To find key from the value in an dictionary 
    for k,v in dictionary.items(): 
        if (v == max_element): 
            key = k 
    return key 