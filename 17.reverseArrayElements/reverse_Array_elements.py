#17. Write a function that takes an unsorted integer
#  array as input and prints the contents of the array in reverse order.
import FindLenght
def reverseContentofAnArray(array):
    i = 1
    lenghtOfArray = FindLenght.count(array)
    print("Printing the Content of the array in reverse order ")
    while (i!=lenghtOfArray):
        print(array[-i])
        i += 1
    print(array[0])
print("---------------------------------------------")
array = [2,1,5,7,3]
reverseContentofAnArray(array)
print("---------------------------------------------")