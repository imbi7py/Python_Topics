# # Creating Named Tuples
# # We are going to create a Point named tuple that will contain an x-coordinate and a y-coordinate.
#
# c_ Point3D
#     ___ __init__ ___  x y z
#         ___.x _ x
#         ___.y _ y
#         ___.z _ z
#
# f__ c.. ____ n..t..
#
# Point2D = n..t.. 'Point2D' 'x' 'y'
#
# # Note that we have two different uses of Point2D here. The label we are assigning the return value of the call to
# # namedtuple and the name of the class generated by calling namedtuple.
# # We could also have done the following:
#
# Pt _ n..t..('Point2D' 'x' 'y'
#
# # The namedtuple class name is Point2D, but the label we Pt simply points to that class, so we would then create
# # instances of the Point2D class as follows:
#
# pt1 = Pt 10 20
#
# # And we can see what pt1 is:
#
# print pt1
# # Point2D(x=10, y=20)
#
# # As you can see we have an object of type Point2D, and it has two properties, x and y with respective values 10 and 20.
# # The only weird thing here is that we are using Pt to generate our instances of the Point2D class.
# # That's why we usually always created namedtuple generated classes this way:
#
# Point2D _ n..t.. 'Point2D' 'x' 'y'
#
# # Then the following makes more sense:
#
# pt1 _ P.2. 10 20
# print pt1
# # Point2D(x=10, y=20)
#
# # This is not different than doing this:
#
# Pt3 _ Point3D  # class we defined earlier
# pt3 _ Pt3 10 20 30
# print(pt3)
#
# # <__main__.Point3D at 0x27408e1fa90>
#
# # As you can see above, we used another label Pt3 as a label that also references the Point3D class. It would be weird to do it this way here, and its weird for tuples as well. Of course, you may run into circumstances where you need to do this - just not as a general rule.
# # Note that all named tuples are honest to goodness classes, just as if you had used a class definition such as with Point3D.
# # The namedtuple function generates classes for us - it is a class factory.
#
# print ty.. P..3.
# # type
#
# print ty.. P.2.
# # type
#
# # However, Point2D is a subclass of tuple, while Point3D is not:
#
# print isi... pt1 tu..
# # True
#
# print isi... pt3 tu..
# # False
#
# # So, when we create an instance of a class, we are in fact calling the __new__ method with our initial values.
# # It's just a callable that has the field names we used to generate our named tuple class as its parameters.
# # This means we can use keyword arguments when instantiating our named tuples!
#
# pt4 _ P.2. y_20 x_10
# print pt4
# # Point2D(x=10, y=20)
#
# # What did we get for free using a named tuple vs our own class?
# # First using a named tuple for our 2D point:
#
# pt2d_1 _ P..2. 10 20
# pt2d_2 _ P.2. 10 20
#
# pt2d_1
# # Point2D(x=10, y=20)
#
# pt2d_1 __ pt2d_2
# # True
#
# # Now using our 3D class:
#
# pt3d_1 _ P..3. 10 20 30
# pt3d_2 _ P..3. 10 20 30
# pt3d_1
# # <__main__.Point3D at 0x27408e1f9e8>
#
# # Oh, we probably need to implement the __repr__ method in our class
#
# pt3d_1 __ pt3d_2
# # False
#
# # And we would also need to implement the eq method!
# # Let's do that:
#
# c_ Point3D
#     ___ __i__ ___ x y z
#         ___.x _ x
#         ___.y _ y
#         ___.z _ z
#
#     ___ __re__ ___
#         r_ _"P.3.|x+|___.x| y_|___.y| z_|___.z||"
#
#     ___ __eq__ ___ other
#         i_ isi... o.. P..3.
#             r_ ___.x __ o__.x an. ___.y __ o__.y an. ___.z __ o__.z
#         e..
#             r_ F..
#
# pt3d_1 _ P..3. 10 20 30
# pt3d_2 _ P..3. 10 20 30
# pt3d_1
# # Point3D(x=10, y=20, z=30)
#
# pt3d_1 __ pt3d_2
# # True
#
# # How about finding the largest coordinate in the point?
# # That's easy for Point2D since it is a tuple, but not the case for Point3D:
#
# ma. pt2d_1
# # 20
#
# # max(pt3d_1) # ERROR TypeError: 'Point3D' object is not iterable
#
# # How about calculating the dot product of two points (considering them as vectors starting at the origin)?
# # The formula would be: a.b = a.x * b.x + a.y + b.y + a.z * b.z
# # For the 3D point we would need to do the following:
#
# ___ dot_product_3d a b
#     r_ a.x * b.x + a.y * b.y + a.z + b.z
#
# d.... pt3d_1 pt3d_2
# # 560
#
# # But for our 2D point, which, remember is a tuple as well, we can write a generic function that would work equally well with a 3D named tuple too:
#
# ___ dot_product a b
#     r_ su.|e 0 * e 1 ___ e i_  zi. a b
#
# # Here's a break down of how we implemented the dot product:
# # First we zip up the components of a and b to get an iterable of tuples containing the x-coordinates in the 1st element, and the y-coordinates in the second tuple. Our zip will contain as many elements as there are dimensions.
#
# a _ P..2. 1 2
# b _ P..2. 10 20
# print(a)
# print(b)
# print(tu..(a))
# print(tu..(b))
# print(list(zip(a, b)))
#
# # Point2D(x=1, y=2)
# # Point2D(x=10, y=20)
# # (1, 2)
# # (10, 20)
# # [(1, 10), (2, 20)]
#
# # Note that if we had more dimensions this would work equally well.
# # Suppose we had 3 dimensions:
#
# u = (1, 2, 3)
# v = (10, 20, 30)
# l.. zi. u v
# # [(1, 10), (2, 20), (3, 30)]
#
# # Then we create a comprehension that multiplies the components together:
#
# e 0 * e 1 ___ e i_ zi. a b
# # [10, 40]
#
# # Then we simply add those up:
#
# su. e 0 * e 1 ___ e i_ zi. a b
# # 50
#
# d.._p.. a b
# # 50
#
# # And if we defined a 4D point named tuple:
#
# Point4D = n..t.. 'P..4.' |'i' 'j' 'k' 'l'
# pt4d_1 _ 1 1 1 10
# pt4d_2 _ 2 2 2 10
# d.._p.. p..1 p..2
# # 106
#
# # As you can see we got the correct dot product. We could not have done this using our Point3D class!
#
#
