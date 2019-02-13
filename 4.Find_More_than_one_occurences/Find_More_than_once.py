Problem Statement :
====================
    Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
Input :
=======
    An Unsorted Integer Array
  
Output :
========
   True - if the element found more than once
   False - if the element is not found more than once 
Code :
======
def findLenght(a): 
    count = 0
    while(a[count:]):
        count += 1
    return count

def find_more_than_once(array,search_elemnt):
    flag = False
    iteratorValue = 0
    lenght = count(array)
    count = 0
    while (iteratorValue!=lenght):
        if (array[iteratorValue] == search_elemnt):
            count += 1
        iteratorValue += 1
    if count == 2:
        flag = True
    return flag
