class StackUnderflowError(Exception
    pass


___ is_integer(string
    try:
        int(string)
        r_ True
    except ValueError:
        r_ False


___ evaluate(input_data
    __ not input_data:
        r_ []
    defines = {}
    w___ input_data[0][:1] __ ':':
        values = input_data.pop(0).split()
        values.pop()
        values.pop(0)
        key = values.pop(0).lower()
        __ is_integer(key
            raise ValueError("Integers cannot be redefined")
        defines[key] = values
    stack = []
    input_data = input_data[-1].split()
    w___ any(input_data
        word = input_data.pop(0).lower()
        try:
            __ is_integer(word
                stack.append(int(word))
            ____ word in defines:
                input_data = defines[word] + input_data
            ____ word __ '+':
                stack.append(stack.pop() + stack.pop())
            ____ word __ '-':
                stack.append(-stack.pop() + stack.pop())
            ____ word __ '*':
                stack.append(stack.pop() * stack.pop())
            ____ word __ '/':
                divisor = stack.pop()
                __ divisor __ 0:
                    raise ZeroDivisionError("Attempted to divide by zero")
                stack.append(int(stack.pop() / divisor))
            ____ word __ 'dup':
                stack.append(stack[-1])
            ____ word __ 'drop':
                stack.pop()
            ____ word __ 'swap':
                stack.append(stack[-2])
                del stack[-3]
            ____ word __ 'over':
                stack.append(stack[-2])
            ____
                raise ValueError("{} has not been defined".format(word))
        except IndexError:
            raise StackUnderflowError("Insufficient number of items in stack")
    r_ stack
