# To find the max of dictionary values 

 Problem :
=========
      To find the min of dictionary values
Input :
=======
    Unsorted Array Elements

 Output :
========
    Maximum Element in an Unsorted Array

 My Way of Solving the Problem (Algorithm) :
===========================================
    1.Find the lenght of the array using Findlenght function written by me.
    2.Set the updated maximum variable by comparing the first two elements in the array
    3.using while loop update updated maximum value untill iterating the entrire array
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
