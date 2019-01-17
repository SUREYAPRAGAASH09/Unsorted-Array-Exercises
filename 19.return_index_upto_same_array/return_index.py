
def array12(array1,i):
    return array1[i]

def array13(array2,i):
    return array2[i]


def return_index(array1,array2):
    flag = True
    i = 0
    while (flag):
        if ((array12(array1,i)) == (array13(array2,i))):
            print (i)
            i += 1
            flag = True
        else:
            flag = False
    return -1

array1 = [1,4,2,6,0]
array2 = [7,5,2,8,5]
print(return_index(array1,array2))
