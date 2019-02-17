Question :
==========
     Given an unsorted integer array A,find the number of times the smallest number is found in the array.
Input :
=======
    Unsorted Array Elements
Output :
========
    Get the largest Number occurence and it's Count value
 
Code :
======
import Max
import FindLenght
def count_a_particular_number(array,max): #max is the number that we have to count 
    count = 0
    iterator = 0
    lenght = FindLenght.count(array)
    while (iterator!=lenght):
        if (array[iterator]==max):
            count += 1
        iterator += 1
    return count

def find_largest_numbers_occurences(array): #Main method 
    max = Max.max(array)
    count = count_occuences(array,max)
    return count
