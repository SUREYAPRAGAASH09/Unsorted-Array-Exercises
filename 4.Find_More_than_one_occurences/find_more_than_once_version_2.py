def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

def find_more_than_once(array,search_elemnt):
    flag = False
    i = 0
    b = count(array)
    counti = 0
    while (i!=b ):
        if (array[i] == search_elemnt ):
            if(counti == 1):
                flag = True
                break
            counti += 1
        i += 1
    return flag

array = [4,2,7,9,3,0,3]
search_elemnt = 3
print(find_more_than_once(array,search_elemnt))