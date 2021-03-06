# # %%
# '''
# # Dynamic Array Exercise
# ____
# 
# In this exercise we will create our own Dynamic Array class!
# We'll be using a built in library called [ctypes](https://docs.python.org/2/library/ctypes.html).
# Check out the documentation for more info, but its basically going to be used here as a raw array from
# the ctypes module.
# If you find yourself very interested in it, check out:
# [Ctypes Tutorial](http://starship.python.net/crew/theller/ctypes/tutorial.html)
# 
# Also...
# '''
# 
# # %%
# '''
# **A quick note on public vs private methods, we can use an underscore _ before the method name to keep it non-public. 
# For example:**
# '''
# 
# 
# # %%
# c_ M o..
# 
#     ___ public ____
#         print('Use Tab to see me!')
# 
#     ___ _private ____
#         print("You won't be able to Tab to see me!")
# 
# 
# # %%
# m = ?
# 
# # %%
# ?.p...
# 
# # %%
# ?._p..
# 
# print()
# print()
# # %%
# '''
# Check out PEP 8 and the Python docs for more info on this!
# _____
# 
# ### Dynamic Array Implementation
# '''
# 
# # %%
# _________ ct...
#
# 
# c_ DynamicArray o..
#     '''
#     DYNAMIC ARRAY CLASS (Similar to Python List)
#     '''
# 
#     ___ -
#         n _ 0  # Count actual elements (Default is 0)
#         capacity _ 1  # Default Capacity
#         A _ m_a.. c...
# 
#     ___ -  ____
#         """
#         Return number of elements sorted in array
#         """
#         r_ n
# 
#     ___ -g k
#         """
#         Return element at index k
#         """
#         __ no. 0 <_ k < n
#             r_ I...('K is out of bounds!')  # Check it k index is in bounds of array
# 
#         r_ A k  # Retrieve from array at index k
# 
#     ___ append ele
#         """
#         Add element to end of the array
#         """
#         __ n __ c...
#             _res..(2 * ca..  # Double capacity if not enough room
# 
#         A n _ e..  # Set ____.n index to element
#         n +_ 1
# 
#     ___ _resize new_cap
#         """
#         Resize internal array to capacity new_cap
#         """
# 
#         B _ make_array n..  # New bigger array
# 
#         ___ k __ ra.. n  # Reference all existing values
#             B k _ A k
# 
#         A _ B  # Call A the new bigger array
#         c... = n...  # Reset the capacity
# 
#     ___ make_array new_cap
#         """
#         Returns a new array with new_cap capacity
#         """
#         r_ |n.. * ct___.py_object
# 
# 
# # %%
# # Instantiate
# arr = ?
# 
# # %%
# # Append new element
# ?.? 1
# 
# # %%
# # Check length
# print ? ?
# 
# # %%
# # Append new element
# ? ? 2
# 
# # %%
# # Check length
# print ? ?
# 
# # %%
# # Index
# print ? 0
# 
# # %%
# print ? 1
# 
# # %%
# '''
# Awesome, we made our own dynamic array! Play around with it and see how it auto-resizes. 
# Try using the same **sys.getsizeof()** function we worked with previously!
# '''
# 
# # %%
# '''
# # Great Job!
# '''
