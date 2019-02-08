Question :
==========
    Given an unsorted integer array and an integer value X as input, return the count of the values less than or equal to X. 
Input :
=======
    Unsorted array - List in Python 
Output :
========
    Search Element upto less than or equal to - Integer
Code :
======
import FindLenght
def validate(array,searchElement):
    add = array[0] + array[1]
    iterator = 2
    Lenght = FindLenght.count(array)
    
    while (iterator!=Lenght):
        add = add + array[iterator]
        if (add >= searchElement):
            break
    return add
