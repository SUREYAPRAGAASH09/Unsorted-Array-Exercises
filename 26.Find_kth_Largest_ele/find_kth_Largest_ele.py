Question : 
==========
       Find the kth largest Element in an array
Input :
=======
    Unsorted Array - List in Python 
Output :
========
    Kth Largest Element - Integer
Code :
======
import Max
import FindLenght
def kth_largest_ele(array,kthelement):
    lenght = FindLenght.count(array)
    iterator = 1
    while(iterator!=kthelement):
        largestElemnt = Max.Max(array)
        for element in array:
            if (element == largestElement):
                 array.remove(largestElement)
         iterator += 1
    largestElement = Max.Max(array)
    return largestElement
