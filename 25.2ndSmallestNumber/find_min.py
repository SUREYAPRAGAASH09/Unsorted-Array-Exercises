 # To find the min of list of values 
 Problem :
=========
      To find the min element from array of elements

Input :
=======
    Unsorted Array Elements - List

Output :
========
    Maximum Element in an Unsorted Array - Integer
Code :
======
import FindLenght
def findMaxrray):
    Array_lenght = FindLenght.len(values) 
    if (Array[0] < Array[1]): 
        Updated_maximum = array[0]
    else: 
        Updated_maximum = Array[1]
    iterator = 2 
    while(iterator!=Array_lenght): 
        if (Array[iterator]<Updated_maximum): 
            Updated_maximum = Array[iterator] 
        iterator += 1 
    return Updated_maximum
