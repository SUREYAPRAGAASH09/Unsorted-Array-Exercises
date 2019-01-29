def test_array1_array2retutn1False():
    #arrange
    array1 = [2,9,1,4,5,]
    array2 = [2,9,1,4,5]
    excepted = True
    #act
    actual = Compare_Two_Array_Elements.compareArrayElements(array1,array2)
    #assert
    assert excepted == actual