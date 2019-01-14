#8. Given an unsorted integer array A, find the mean.

import Sum
import FindLenght

def mean(array):
    sum = Sum.sum(array)
    print(sum)
    divide_value = FindLenght.count(array)
    mean = sum / divide_value
    return mean

array = [4,2,6,7,3]
print(mean(array))
