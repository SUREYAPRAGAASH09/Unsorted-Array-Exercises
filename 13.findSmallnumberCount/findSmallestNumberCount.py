Question :
==========
     Given an unsorted integer array A,find the number of times the smallest number is found in the array.
Input :
=======
    Unsorted Array Elements
Output :
========
    Get the Smallest Number occurence and it's Count value
Algorithm :
===========
     1.Get the minumum number form the array 
     2.using the count value , count the occruence of that minimum elemet found in that array 
     3.return the count 
Code :
======
import Findmin
import FindLenght
def count_a_particular_number(array,min): #max is the number that we have to count 
    count = 0
    iterator = 0
    lenght = FindLenght.count(array)
    while (iterator!=lenght):
        if (array[iterator]==max):
            count += 1
        iterator += 1
    return count

def find_largest_numbers_occurences(array): #Main method 
    min = Findmin.findmin(array)
    count = count_occuences(array,min)
    return count
