Problem Statement :
===================
    Given an unsorted integer array A and an integer value X, find if X is found more than once in A.
Input :
=======
    Unsorted Integer Array
    
Output :
========
    Integer 0 means No number is found 
    Integer more than 1 means number is found 

def Findlenght(array):
    count = 0
    while(array[count:]):
        count += 1
    return counti

def findOccuenceofElement(array,search_elemnt):
    iteratorValue = 0
    lenght = count(array)
    occurenceValue = 0
    while (iteratorValue!=lenght):
        if (array[iteratorValue] == search_elemnt):
            count += 1
        iteratorValue += 1
    return count
