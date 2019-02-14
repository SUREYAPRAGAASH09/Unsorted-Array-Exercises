Problem Statement :
===================
    Given an unsorted integer array A and a value X, 
    check if there exists a subset of A of size two that adds upto X (Subset sum for a pair)
Input :
=======
    Unsorted Integer Array 
Output :
========
    True - If found any subset pair from the Unsorted Integer Array
    False - If not found any subset pair from the Unsorted Integer Array
Code :
=======
import FindLenght
def subset(array,sumValue):  
    flag = False  
    iteratorValue = 0
    lenght = FindLenght.findLenght(array)
    while (iteratorValue!=lenght):
        indexValue = iteratorValue + 1
        while (indexValue!=lenght):
            if ((array[iteratorValue] + array[indexValue]) == sumValue):
                flag = True
            indexValue += 1
        iteratorValue += 1
    return flag
