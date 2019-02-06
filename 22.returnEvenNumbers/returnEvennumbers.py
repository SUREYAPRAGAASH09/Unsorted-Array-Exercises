Question :
===========
    Given an unsorted integer array as input,  return the number of even numbers in it.
Input :
=======
    Unsorted array elements 
Output :
========
    Returning an array Containing only Even Numbers
Code :
=======
def returnEvennumbers(array):
    evenList = []
    for iterator in array:
        if iterator%2 == 0:
            evenlist.append(iterator)
    return evenList
