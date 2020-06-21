import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields_):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields_ = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields_):
            raise ValueError('{} arguments required'.format(len(cls._fields_)))
        return super().__new__(cls,args)

# Examples
class Stock(StructTuple):
    _fields_ = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields_ = ['x', 'y']

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s[0])
    print(s.name)
    print(s.shares * s.price)
    try:
        s.shares = 23
    except AttributeError as e:
        print(e)

# Problem
# You want to initialize parts of a class definition once at the time a class is defined, not
# when instances are created.
# Solution
# Performing initialization or setup actions at the time of class definition is a classic use
# of metaclasses. Essentially, a metaclass is triggered at the point of a definition, at which
# point you can perform additional steps.
# Here is an example that uses this idea to create classes similar to named tuples from the
# collections module:

# Discussion
# In this recipe, the StructTupleMeta class takes the listing of attribute names in the
# _fields class attribute and turns them into property methods that access a particular
# tuple slot. The operator.itemgetter() function creates an accessor function and the
# property() function turns it into a property.
# The trickiest part of this recipe is knowing when the different initialization steps occur.
# The __init__() method in StructTupleMeta is only called once for each class that is
# defined. The cls argument is the class that has just been defined. Essentially, the code
# is using the _fields class variable to take the newly defined class and add some new
# parts to it.
# The StructTuple class serves as a common base class for users to inherit from. The
# __new__() method in that class is responsible for making new instances. The use of
# __new__() here is a bit unusual, but is partly related to the fact that we’re modifying the
# calling signature of tuples so that we can create instances with code that uses a normallooking
# calling convention like this:
# s = Stock('ACME', 50, 91.1) # OK
# s = Stock(('ACME', 50, 91.1)) # Error
# Unlike __init__(), the __new__() method gets triggered before an instance is created.
# Since tuples are immutable, it’s not possible to make any changes to them once they
# have been created. An __init__() function gets triggered too late in the instance creation
# process to do what we want. That’s why __new__() has been defined.
# Although this is a short recipe, careful study will reward the reader with a deep insight
# about how Python classes are defined, how instances are created, and the points at which
# different methods of metaclasses and classes are invoked.
# PEP 422 may provide an alternative means for performing the task described in this
# recipe. However, as of this writing, it has not been adopted or accepted. Nevertheless,
# it might be worth a look in case you’re working with a version of Python newer than
# Python 3.3.