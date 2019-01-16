#12. Given an unsorted integer array A, 
# find the number of times the smallest number is found in the array.
import find_min
import FindLenght
def count_occuences(array,min):
    count = 0
    i = 0
    lenght = FindLenght.count(array)
    while (i!=lenght):
        if (array[i]==min):
            count += 1
        i += 1
    return count

def find_Smallest_numbers_occurences(array):
    min = find_min.find_smallest_value(array)
    count = count_occuences(array,min)
    return count
array = [3,8,3,7,9]
print(find_Smallest_numbers_occurences(array))
