import FindLenght
def subset(array,sum):  
    flag = False  
    i = 0
    lenght = FindLenght.count(array)
    while (i!=lenght):
        j = i + 1
        while (j!=lenght):
            if ((array[i] + array[j]) == sum):
                flag = True
            j += 1
        i += 1
    return flag

print("==========================")
array = [5,7,8,2,6,5,8]
sum = 16
subset(array,sum)
print("=============================")
