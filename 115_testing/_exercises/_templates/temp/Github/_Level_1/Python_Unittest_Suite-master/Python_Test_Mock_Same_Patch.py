# Python Test Mock
# unittest.mock � mock object library
# unittest.mock is a library for testing in Python.
# It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
# unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite.
# After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with.
# You can also specify return values and set needed attributes in the normal way.
# 
# Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel
# for creating unique objects.
# 
# Mock is very easy to use and is designed for use with unittest. Mock is based on the �action -> assertion� pattern instead of �record -> replay� used by
# many mocking frameworks.
#

#
# Applying the same patch to every test method:
# 
# If you want several patches in place for multiple test methods the obvious way is to apply the patch decorators to every method.
# This can feel like unnecessary repetition. For Python 2.6 or more recent you can use patch() (in all its various forms) as a class decorator.
# This applies the patches to all test methods on the class.
# A test method is identified by methods whose names start with test:
# 

@patch('mymodule.SomeClass')

    c_ MyTest(TestCase):

        ___ test_one  MockSomeClass):
            assertIs(mymodule.SomeClass, MockSomeClass)

        ___ test_two  MockSomeClass):
            assertIs(mymodule.SomeClass, MockSomeClass)

        ___ not_a_test
            r_ 'something'

MyTest('test_one').test_one()
MyTest('test_two').test_two()

MyTest('test_two').not_a_test()

# OUTPUT: 'something'
 
#
# An alternative way of managing patches is to use the patch methods: start and stop.
# These allow you to move the patching into your setUp and tearDown methods.
# 

c_ MyTest(TestCase):

        ___ setUp
            patcher _ patch('mymodule.foo')

            mock_foo _ patcher.start()

        ___ test_foo
            assertIs(mymodule.foo, mock_foo)

        ___ tearDown
            patcher.stop()

MyTest('test_foo').run()

# 
# If you use this technique you must ensure that the patching is �undone� by calling stop.
# This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called. unittest.TestCase.addCleanup()
# makes this easier:
# 

c_ MyTest(TestCase):

        ___ setUp
            patcher _ patch('mymodule.foo')

            addCleanup(patcher.stop)
            mock_foo _ patcher.start()

        ___ test_foo
            assertIs(mymodule.foo, mock_foo)

MyTest('test_foo').run()
