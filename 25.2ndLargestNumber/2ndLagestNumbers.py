Question :
==========
    Get Second largest number form the list
Input :
=======
    Unsorted Integer Array
Output :
========
    Integer - Get second largest integer
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
