import FindLenght
import Max
import Equate
 
def built_dictionary(array): # To Built a dictionary  
    d = {} #creating a empty dictionary 
    count = 0 
    for i in array: 
        count = 1 
        if i in d: 
            d[i] = d[i] + 1 
        else: 
            d[i] = count  
    return d 

def find_key_from_dictionary(dictionary,max_element): # To find key from the value in an dictionary 
    for k,v in dictionary.items(): 
        if (v == max_element): 
            key = k 
    return key 

def find_most_occureence(array): # the main function  
    dictionary = built_dictionary(array) 
    values = list(dictionary.values()) # converting the dictonary value to a list 
    if (Equate.Equate(values)):
        max_element = Max.Max(values)  
        key = find_key_from_dictionary(dictionary,max_element) 
        print ("the number {1} appears {0} times".format(max_element,key))
    else:
        print ("Can't find the most occurence of an element")


#array = [1,2,5,3,2,4,5,5,5] 
#array = [2,6,2,7,2,8,2]
#array = [4,3,2,4,5,4]
array = [1,2,3,4,5]
find_most_occureence(array)