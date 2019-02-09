Question :
==========
    Given an unsorted integer array A and an integer value X, return the index at which X is located in A or return -1 if it is not found in A.
Input :
=======
    Unsorted array - List in Python 
Output :
========
    Return Index - Integer 
Code :
=======
def getIndex(array,indexFor):
    index = 0
    iterator = 0
    lennght = len(array) # Lenght function is used - inbuilt method  
    while (iterator!=lennght):
        if (array[iterator] == indexFor):
            break
        index += 1
        iterator += 1
    return index
