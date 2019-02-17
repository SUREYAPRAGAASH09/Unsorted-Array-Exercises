'''Problem Statement :
===================
    Given an unsorted integer array, 
    return the count of the elements with values that falls within a given range.

Input :
=======
   unsorted integer array

Output :
========
    count values - integer

Code :
======'''
def findLenght(array):
    count = 0
    while(array[count:]):
        count += 1   
    return count

def Countrangeofelements(rangeArray,array):
    countValue = 0
    iteratorValue = 0
    Lenght = findLenght(rangeArray)
    while(iteratorValue != Lenght):
        if rangeArray[iteratorValue] in array :
            countValue += 1
        iteratorValue += 1
    return countValue
