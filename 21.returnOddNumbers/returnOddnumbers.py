#21. Given an unsorted integer array as input,  return the number of odd numbers in it.

def returnOddnumbers(array):
    odd = []
    for i in array:
        if i%2 == 1:
            odd.append(i)
    return odd

array = [5,3.2,33,2,2,7,4,9]
print (returnOddnumbers(array))