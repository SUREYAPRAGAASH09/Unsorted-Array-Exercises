#17. Write a function that takes an unsorted integer
#  array as input and prints the contents of the array in reverse order.
Input :
=======
    Unsorted Array Elements
Output :
========
    Reversed Unsorted Array Elements 
My logic:
===========
    1.Count the No of elements in the array
    2.iterate the whole array using a[-i] using while loop untill the complete array get ends
    3.print the array[0] Element 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
import FindLenght
def reverseContentofAnArray(array):
    iterator = 1
    lenghtOfArray = FindLenght.count(array)
    print("Printing the Content of the array in reverse order ")
    while (iterator!=lenghtOfArray):
        print(array[-iterator])
        iterator += 1
    print(array[0])
print("---------------------------------------------")
array = [2,1,5,7,3]
reverseContentofAnArray(array)
print("---------------------------------------------")
