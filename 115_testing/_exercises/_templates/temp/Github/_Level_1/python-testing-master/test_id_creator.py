______ u__
____ u__ ______ TestCase

____ id_creator ______ IdCreator


c_ TestIdCreator(TestCase
    """
    Tests for the IdCreator.
    See id_creator.py
    """
    id_creator _ IdCreator()

    ___ test_valid_value_one
        aE..(1, id_creator.faculty_id(1))

    ___ test_valid_value_zero
        aE..(1, id_creator.faculty_id(0))

    ___ test_valid_value_three
        aE..(6, id_creator.faculty_id(3))

    ___ test_invalid_value_error
        w__ aR..(TypeError
            id_creator.faculty_id('a')

    ___ test_invalid_type_error
        w__ aR..(V..
            id_creator.faculty_id(-1)


__ __name__ __ '__main__':
    ?.?
