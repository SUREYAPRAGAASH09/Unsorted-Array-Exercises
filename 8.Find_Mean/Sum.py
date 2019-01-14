#Given an unsorted integer array A, find the sum of all the elements in A
#input = array of any size
#output = sum of all the element of the given array

import FindLenght

def sum(array):
    lenght_of_an_array = FindLenght.count(array)
    sum = 0
    i = 0
    while(i!=lenght_of_an_array):
        sum  = sum + array[i]
        i += 1
    return sum 

#array = [1,5,3,6,7,3]
#print(sum(array))
