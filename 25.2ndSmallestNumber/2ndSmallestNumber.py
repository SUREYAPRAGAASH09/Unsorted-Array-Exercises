Question :
==========
    find minimum element from the list of elements
 Input :
========
    List of Unsorted Array elements
Output :
========
    Integer - minimum element from the list
Code :
======
import find_min
def secondsmallestNumber(array):
    minimum_element = find_min.findMin(array)
    for iterator in array:
        if minimum_element == iterator:
            array.remove(iterator)
    minimum_element = find_min.findMin(array)
    return minimum_element
