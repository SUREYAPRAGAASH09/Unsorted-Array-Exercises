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
def findLenght(array):
    count = 0
    while(array[count:]):
        count += 1
    return count

def find_more_than_once(array,search_elemnt):
    flag = False
    iteratorValue = 0
    lenght = findlenght(array)
    count = 0
    while (iteratorValue!=lenght ):
        if (array[iteratorValue] == search_elemnt ):
            if(count == 1):
                flag = True
                break
            count += 1
        iteratorValue += 1
    return flag
