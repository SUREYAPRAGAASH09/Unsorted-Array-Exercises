import isContain

def test_AssertTrue(): # Environment Test
    assert True


def test_array_retutn_5():
    #arrange
    array = [3,5,7,9,0,3]
    Search_element = 3
    excepted = True
    #act
    actual = isContain.find_element(array,Search_element)
    #assert
    assert excepted == actual 

def test_array1_retutn_5():
    #arrange
    array = [3,5,7,9,0,3]
    Search_element = 9
    excepted = True
    #act
    actual = isContain.find_element(array,Search_element)
    #assert
    assert excepted == actual
