Question :
==========
    Get the 2nd largest number form the list
Input :
=======
    Unsorted Array
Output :
========
    Integer - Get 2nd largest number 
Code :
======
import Max 
def secondLargestNumber(array):
    Maximum = Max.Max(array)
    for iterator in array:
        if Maximum == iterator:
            array.remove(iterator)
    maximum = Max.Max(array)
    return maximum
