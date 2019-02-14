Problem Statement :
===================    
    Given an unsorted integer array A, find the sum of all the elements in A
Input :
=======    
    Unsorted Integer array 
Output :
========    
    sum of all the element - Integer 
Code :
======    
import FindLenght

def sum(array):
    sumValue = 0
    iteratorValue = 0
    while(iteratorValue!=FindLenght.count(array)):
        sumValue  =+ array[iteratorValue]
        iteratorValue += 1
    return sumValue 

