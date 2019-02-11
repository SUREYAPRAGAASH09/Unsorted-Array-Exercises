Question :
==========
    Shift Greater than N elements in an array 
Input :
=======
    Unsorted Integer Array
Output :
=========
    Unsorted Integer Array but, After shifting greater than n elements in an arrray
Code :
=======
def swapRight(array,shiftValue):
    if (shiftValue > len(array)):
        shiftValue = shiftValue - len(array)
    
    temp = 0
    j = 0
    while (j!=shiftValue):
        i = -1
        while (i!=len(array)):
            array[i],temp = temp,array[i]
            i += 1
        j += 1
    return array

def shiftLeft(array,shiftValue):
    if (shiftValue > len(array)):
        shiftValue = shiftValue - len(array)
    i = 0
    while(i!=shiftValue):
        j = 0
        temp = (array[j])
        array.remove(array[j])
        array.append(temp)
        i+=1
    return array
