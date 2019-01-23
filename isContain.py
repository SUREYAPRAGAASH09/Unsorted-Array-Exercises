#to find the element whether it is present or not 
def find_element(array,search_element):
    for i in array:
        flag = False
        if (i==search_element):
            flag = True
            break
    return flag

array = [3,5,7,9,0,3]
search_element = 3
print(find_element(array,search_element)) 
