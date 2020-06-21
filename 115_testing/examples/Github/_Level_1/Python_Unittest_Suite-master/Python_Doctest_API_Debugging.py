# Python Doctest API
# The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work
# exactly as shown.
#
#  There are several common ways to use doctest:
# > To check that a module�s docstrings are up-to-date by verifying that all interactive examples still work as documented.
# > To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
# > To write tutorial documentation for a package, liberally illustrated with input-output examples.
#   Depending on whether the examples or the expository text are emphasized, this has the flavor of �literate testing� or �executable documentation�.
#

#
# Debugging:
# Doctest provides several mechanisms for debugging doctest examples:
# > Several functions convert doctests to executable Python programs, which can be run under the Python debugger, pdb.
# > The DebugRunner class is a subclass of DocTestRunner that raises an exception for the first failing example, containing information about that example.
#   This information can be used to perform post-mortem debugging on the example.
# > The unittest cases generated by DocTestSuite() support the debug() method defined by unittest.TestCase.
# > You can add a call to pdb.set_trace() in a doctest example, and you�ll drop into the Python debugger when that line is executed.
#   Then you can inspect current values of variables, and so on. For example, suppose a.py contains just this module docstring:
# 

"""
>>> def f(x):
...     g(x*2)
>>> def g(x):
...     print(x+3)
...     import pdb; pdb.set_trace()
>>> f(3)
9
"""
 
#
# Then an interactive Python session may look like this:
# 

import a, doctest

doctest.testmod(a)
