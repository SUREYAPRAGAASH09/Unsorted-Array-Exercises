#To find the lenght of an array using slicing methodogy

def count(a):
    counti = 0
    while(a[counti:]):
        counti += 1

    return counti

array = [1,5,4,5,9]
print(count(array)) 
