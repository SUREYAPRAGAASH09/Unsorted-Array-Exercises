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
    shiftValue = 0
    while(shiftValue!=1):
        temp = (array[0])
        array.remove(array[0])
        array.append(temp)
        shiftValue+=1
    return array
