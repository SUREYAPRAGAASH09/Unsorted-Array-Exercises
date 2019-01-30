import getindexAterrotation
def test_assertTrue():
    assert True

def test_indexvalue_rotationvalue_return_9():
    #arrange
    array = [5,7,6,9,2,8]
    index = 2
    rotation_value = 1
    excepted = 9
    #act
    actual = getindexAterrotation.getIndexAfterrotationLeft(array,index,rotation_value)
    #assert
    assert excepted == actual 

def test_indexvalue_rotationvalue_return_6():
    #arrange
    array = [5,7,6,9,2,8]
    index = 1
    rotation_value = 1
    excepted = 6
    #act
    actual = getindexAterrotation.getIndexAfterrotationLeft(array,index,rotation_value)
    #assert
    assert excepted == actual 