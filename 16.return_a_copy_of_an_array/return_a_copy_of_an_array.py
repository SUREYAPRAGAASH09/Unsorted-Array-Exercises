#16. Wrtie a function that takes an unsorted integer array as input and returns a copy of the array as output.

def produce_copy(array):
    copy_array = []
    for i in array:
        copy_array.append(i)

    return copy_array

array = [3,1,6,8,9]
print(produce_copy(array))