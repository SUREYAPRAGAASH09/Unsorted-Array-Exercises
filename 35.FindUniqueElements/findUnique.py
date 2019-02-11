Question :
==========
    Given an unsorted integer array A containing  elements from 0-9, find the number of unique elements.
Input :
=======
    Unsorted Integer Array
Output :
========
    Get Uniques in integer Array
Code :
======
import find_min
import dictionaryOperations
def findUnique(array):
    dictionary = dictionaryOperations.built_dictionary(array)
    listValues = list(dictionary.values())
    minimum_value = find_min.findMin(listValues)
    for iterator in listValues:
        if iterator == minimum_value :
            min = (dictionaryOperations.find_key_from_dictionary(dictionary,i))
            print(min)
            dictionary.pop(min)
 
