import isContain

def test_AssertTrue():
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