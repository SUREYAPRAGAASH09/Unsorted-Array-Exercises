#Sub Module for Finding Unique Elements
def built_dictionary(array):   
    dictionary = {} #creating a empty dictionary 
    count = 0 
    for iterator in array: 
        count = 1 
        if iterator in dictionary: 
            dictionary[iterator] = dictionary[iterator] + 1 
        else: 
            dictionary[iterator] = count  
    return dictionary

def find_key_from_dictionary(dictionary,max_element): # To find key from the value in an dictionary 
    for KEY,VALUE in dictionary.items(): 
        if (VALUE == max_element): 
            key = KEY 
    return key 
