import return_a_copy_of_an_array

def test_assertTrue():
    assert True

def test_arrayreturnarray():
    #arrange
    array = [7,4,2,8,2,0]
    excepted = [7,4,2,8,2,0]
    #act
    actual = return_a_copy_of_an_array.produce_copy(array)
    #assert
    assert excepted == actual

    