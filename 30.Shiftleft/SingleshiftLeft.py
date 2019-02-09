Question :
==========
    Shift the number to the left hand side for only one time 
Input :
=======
    Unsorted Array - list in Python
Output :
========
    List in Python after single time left hand side shift operation overd 
Code :
======
def shiftLeft(array):
    iterator = 0
    while(iterator!=1):
        iterator2 = 0
        temp = (array[iterator2])
        array.remove(array[iterator2])
        array.append(temp)
        iterator+=1
    return array
