______ unittest
____ circle ______ circle_area
____ circle ______ circle_circumfrence
____ math ______ pi

# https://www.youtube.com/watch?v=1Lfv5tUGsn8

c_ TestCircleArea(unittest.TestCase):
    ___ test_area
        # Tests to confirm that it calculates the area as expected
        assertAlmostEqual(circle_area(0),0)
        assertAlmostEqual(circle_area(2), pi*(2**2))
        assertAlmostEqual(circle_area(3.145),pi*(3.145**2))
    
    ___ test_area_types
        # Test to make sure the correct type is entered into the function
        assertRaises(TypeError, circle_area, "Text")
        assertRaises(TypeError, circle_area, True)
        assertRaises(TypeError, circle_area, 5+3j)

    ___ test_area_values
        # Test to make sure the incorrect value hasnt been entered
        assertRaises(ValueError, circle_area, -3)

    ___ test_circumfrence
        # Tests circumfrence to expected val
        assertAlmostEqual(circle_circumfrence(0), 0)      
        assertAlmostEqual(circle_circumfrence(2), 2*pi*2)
        assertAlmostEqual(circle_circumfrence(3.14556445), 3.14556445*pi*2)

    ___ test_circumfrence_types
        # Test circumfrence input to make sure errors handled
        assertRaises(TypeError, circle_circumfrence, "Text")
        assertRaises(TypeError, circle_circumfrence, True)
        assertRaises(TypeError, circle_circumfrence, 3+4j)

    ___ test_circumfrence_values
        # Test to insure proper type is entered into value
        assertRaises(ValueError, circle_circumfrence, -3)
        assertRaises(ValueError, circle_circumfrence, -99.23545)







