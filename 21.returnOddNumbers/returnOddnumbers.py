Question :
===========
    Given an unsorted integer array as input,  return the number of odd numbers in it.
Input :
=======
    Unsorted Integer Array 
Output :
========
    return only the odd numbers as an array 
Code :
======
def returnOddNumbers(array):
    oddList = []
    for iteratorValue in array:
        if iteratorValue%2 == 1:
            oddList.append(iteratorValue)
    return oddList
