Question :
==========
    Given an unsorted integer array and an integer value X as input, return the count of the values greater than or equal to X.
Input :
=======
    unsorted Array - List in Python 
Output :
========

import FindLenght
def validate(array,searchElementX):
    #add = array[0] + array[1]
    iterator = 0
    Lenght = FindLenght.count(array)
    add = 0
    while (add>=searchElemntX):
        add = add + array[i]
        iterator += 1            
    return add 
