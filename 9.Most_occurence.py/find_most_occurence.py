import FindLenght
import Max
import Equate
 
def built_dictionary(array): # To Built a dictionary  
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
    for key,value in dictionary.items(): 
        if (value == max_element): 
            keys = key 
    return keys 

def find_most_occureence(array): # the main function  
    dictionary = built_dictionary(array) 
    values = list(dictionary.values()) # converting the dictonary value to a list 
    if (Equate.Equate(values)):
        max_element = Max.Max(values)  
        key = find_key_from_dictionary(dictionary,max_element) 
        print ("the number {1} appears {0} times".format(max_element,key))
    else:
        print ("Can't find the most occurence of an element")
