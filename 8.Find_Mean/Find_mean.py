Problem Statement :
===================    
    Given an unsorted integer array A, find the mean.
Input :
=======
    Unsorted Integer array
Output :
========
    Integer - Mean Value
Code :
======    
import Sum
import FindLenght

def mean(array):
        return Sum.sum(array)/FindLenght.findLenght(array)

