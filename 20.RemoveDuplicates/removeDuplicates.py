Question :
==========
    Remove Dupliocate from the array
Input :
=======
    Unsorted Integer Array 
Output :
========
    Get a array of not having dulicate array elements
Code :
=======
def removeDuplicate(array):   
    dictionary = {}  
    count = 0 
    for itertorValue in array: 
        count = 1 
        if iteratorValue in dictionary: 
            dictionary[iteratorValue] = dictionary[iteratorValue] + 1 
        else: 
            dictionary[iteratorValue] = count  
    return list(dictionary.keys())
