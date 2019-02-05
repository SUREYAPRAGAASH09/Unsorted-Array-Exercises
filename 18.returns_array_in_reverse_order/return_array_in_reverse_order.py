Question :
==========
    Write a function that takes an unsorted integer array as input and returns an array with the values in reverse order.
Input :
=======
     unsorted array 
Ouput :
=======
     Reversed Unsorted array 
Algorithm :
===========
      1. Initialize a empty array 
      2. Using append function append all the elemnet in to the empty array using -i attribute value 
      3. return that reversed unsorted array as output 
Code :
======
 import FindLenght
def returnContentInReverseOrder(array):
    ReversedArray = []
    iterator = 1
    lenght = FindLenght.count(array)
    while (iterator!=lenght):
        ReversedArray.append(array[-iterator])
        iterator += 1
    ReversedArray.append(array[0])

    return ReversedArray
