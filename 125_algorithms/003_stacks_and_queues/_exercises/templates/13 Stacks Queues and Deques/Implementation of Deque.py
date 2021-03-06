# # %%
# '''
# # Implementation of Deque
# In this lecture we will implement our own Deque class!
# ## Methods and Attributes
# * Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
# * addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
# * addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
# * removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
# * removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
# * isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
# * size() returns the number of items in the deque. It needs no parameters and returns an integer.
#
# ## Deque Implementation
# '''
#
# # %%
# c_ Deque
#     ___ -
#         items     # list
#
#     ___ isEmpty
#         r_ ? __  # list
#
#     ___ addFront item
#         ?.ap.. ?
#
#     ___ addRear item
#         ?.i.. 0 ?
#
#     ___ removeFront
#         r_ ?.p..
#
#     ___ removeRear
#         r_ ?.p.. 0
#
#     ___ size
#         r_ le. ?
#
# # %%
# d = ?
#
# # %%
# ?.a F.. 'hello'
#
# # %%
# ?.aR.. 'world'
#
# # %%
# ?.s..
#
# # %%
# print ?.rF.. + ' ' +  ?.rR..
#
# # %%
# ?.s...
#
# # %%
# '''
# ## Good Job!
# '''
