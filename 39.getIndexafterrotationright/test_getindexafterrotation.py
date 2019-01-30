import getindexRight
def test_assertTrue():
    assert True

def test_indexvalue_rotationvalue_return_7():
    #arrange
    array = [5,7,6,9,2,8]
    index = 2
    rotation_value = 1
    excepted = 7
    #act
    actual = getindexRight.getIndexAfterrotationRight(array,index,rotation_value)
    #assert
    assert excepted == actual 

def test_indexvalue_rotationvalue_return_5():
    #arrange
    array = [5,7,6,9,2,8]
    index = 1
    rotation_value = 1
    excepted = 5
    #act
    actual = getindexRight.getIndexAfterrotationRight(array,index,rotation_value)
    #assert
    assert excepted == actual 