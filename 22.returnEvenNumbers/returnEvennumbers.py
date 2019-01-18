#22.  Given an unsorted integer array as input,  return the number of even numbers in it.


def returnEvennumbers(array):
    even = []
    for i in array:
        if i%2 == 0:
            even.append(i)
    return even

array = [12,34,54,67,34,98,12,90,2,4]
print(returnEvennumbers(array))
