#Given an unsorted integer array A, find the sum of all the elements in A
#input = array of any size
#output = sum of all the element of the given array

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def sum(array):
    lenght_of_an_array = count(array)
    sum = 0
    i = 0
    while(i!=lenght_of_an_array):
        sum  = sum + array[i]
        i += 1
    return sum 


#print(sum(array))
