#27. Given an unsorted integer array and an integer value X
#  as input, return the count of the values less than or equal to X. 
#import FindLenght
def validate(array,search_ele):
    #flag = False
    add = array[0] + array[1]
    i = 2
    #Lenght = FindLenght.count(array)
    
    while (add<=search_ele):
        add = add + array[i]
        i += 1

    return add
array = [5,1,9,7,2,8,3,6,4]
search_ele = 25
print(validate(array,search_ele))