Question :
==========
    Given an unsorted integer array and an integer value X  as input, return the count of the values less than or equal to X. 
Input :
========
    Unsorted Array - List in Python 
Output :
========
    Element less or equal to search element - Integer 
def addUptoElement(array,searchElement):
    Add = array[0] + array[1]
    iterator = 2
    while (Add<=searchElement):
        add = add + array[iterator]
        iterator += 1
    return Add
