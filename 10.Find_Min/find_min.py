Problem :
=========
 To find the min of dictionary values
Input :
=======
    Unsorted Array Elements
Output :
========
    Minimum Element in an Unsorted Array
My Way of Solving the Problem (Algorithm) :
===========================================
    1.Find the lenght of the array using Findlenght function written by me.
    2.Set the updated minumum variable by comparing the first two elements in the array
    3.using while loop update updated minimum value untill iterating the entrire array
Code :
======
import FindLenght
def findMin(Array):
    
    Array_lenght = FindLenght.len(values) 
     
    if (Array[0] < Array[1]): 
        Updated_minimum  = Array[0]
    else: 
        Updated_minimum = Array[1]
    iterator = 2 
    while(iterator!=Array_lenght): 
        if (Array[iterator]<Updated_minimum): 
            Updated_minimum = Array[iterator] 
        iterator += 1 
    return Updated_minimum 


