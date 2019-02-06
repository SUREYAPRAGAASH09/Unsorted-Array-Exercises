Question :
===========
    Given an unsorted integer array as input,  return the number of odd numbers in it.
Input :
=======
    Unsorted Array 
Output :
========
    return only the odd numbers as an array 
Code :
======
def returnOddNumbers(array):
    oddList = []
    for iterator in array:
        if iterator%2 == 1:
            oddList.append(i)
    return oddList
