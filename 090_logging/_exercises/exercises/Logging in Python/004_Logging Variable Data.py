# # Logging Variable Data
# # In most cases, you would want to include dynamic information from your application in the logs. You have seen that
# # the l____ methods take a string as an argument, and it might seem natural to format a string with variable data
# # in a separate line and pass it to the log method. But this can actually be done directly by using a format string for
# # the message and appending the variable data as arguments. Here is an example:
#
# ______ l____
#
# name _ 'John'
# l____.e.. '%s raised an error' ?
# # ERROR:root:John raised an error
#
# # The arguments passed to the method would be included as variable data in the message.
# # While you can use any formatting style, the f-strings introduced in Python 3.6 are an awesome way to format strings
# # as they can help keep the formatting short and easy to read:
#
# ______ l____
# name _ 'John'
#
# l____.e..(_*? raised an error
# # ERROR:root:John raised an error