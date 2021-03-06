# ______ ti..
# ____ fun.. ______ wr..
#
# ____ timethis func
#     '''
#     Decorator that reports the execution time.
#     '''
#     ?w.. ?
#     ___ wrapper $ $$
#         start _ ti__.ti__
#         result _ ? $ $$
#         end _ ti__.ti..
#         print ?. -n e.. - s..
#         r_ ?
#     r_ ?
#
# __ ______ __ ______
#     ??
#     ___ countdown n ?
#         '''
#         Counts down
#         '''
#         w___ n > 0
#             n -_ 1
#
#     ? 100000
#     print('Name:', ?. -n
#     print('Docstring:', re.. ?. -d
#     print('Annotations:', ?. -a
#
# # Problem
# # You’ve written a decorator, but when you apply it to a function, important metadata
# # such as the name, doc string, annotations, and calling signature are lost.
# # Solution
# # Whenever you define a decorator, you should always remember to apply the @wraps
# # decorator from the functools library to the underlying wrapper function. For example:
#
# # Discussion
# # Copying decorator metadata is an important part of writing decorators. If you forget to
# # use @wraps, you’ll find that the decorated function loses all sorts of useful information.
# # For instance, if omitted, the metadata in the last example would look like this:
# # >>> countdown.__name__
# # 'wrapper'
# # >>> countdown.__doc__
# # >>> countdown.__annotations__
# # {}
# # >>>
# # An important feature of the @wraps decorator is that it makes the wrapped function
# # available to you in the __wrapped__ attribute. For example, if you want to access the
# # wrapped function directly, you could do this:
# # >>> countdown.__wrapped__(100000)
# # >>>
# # The presence of the __wrapped__ attribute also makes decorated functions properly
# # expose the underlying signature of the wrapped function. For example:
# # >>> from inspect ______ signature
# # >>> print(signature(countdown))
# # (n:int)
# # >>>
# # One common question that sometimes arises is how to make a decorator that directly
# # copies the calling signature of the original function being wrapped (as opposed to using
# # *args and **kwargs). In general, this is difficult to implement without resorting to some
# # trick involving the generator of code strings and exec(). Frankly, you’re usually best off
# # using @wraps and relying on the fact that the underlying function signature can be
# # propagated by access to the underlying __wrapped__ attribute. See Recipe 9.16 for more
# # information about signatures.
