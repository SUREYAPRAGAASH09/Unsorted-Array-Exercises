Problem Statement :
===================
    Given an unsorted integer array A, find the sum of all the elements in A
Input :
=======    
    Unsorted Integer Array 
Output :
========    
    sum of all the element of the given array - Integer
Code :
=======    
def FindLenght(array):
    count = 0
    while(array[count:]):
        count += 1
    return count

def findSum(array):
    lenght = findlenght(array)
    sumValue = 0
    iteratorValue = 0
    while(iteratorValue!=lenght):
        sumValue  = sumValue + array[iteratorValue]
        iteratorValue += 1
    return sumValue 
