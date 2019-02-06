Question :
==========
    Remove Dupliocate from the array
Input :
=======
    Unsorted Array Elemnts
Output :
========
    Get a array of not having dulicate array elements
Code :
=======
def removeDuplicate(array):   
    dictionary = {}  
    count = 0 
    for itertor in array: 
        count = 1 
        if iterator in d: 
            d[iterator] = d[iterator] + 1 
        else: 
            d[iterator] = count  
    return list(dictionary.keys())
