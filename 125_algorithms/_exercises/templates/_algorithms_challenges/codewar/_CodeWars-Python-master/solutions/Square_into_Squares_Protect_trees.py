"""
Square into Squares. Protect trees!

http://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

"""


___ decompose(n
    goal = 0
    result = [n]
    w___ result:
        current = result.pop()
        goal += current ** 2
        for i in range(current - 1, 0, -1
            __ goal - (i ** 2) >= 0:
                goal -= i ** 2
                result.append(i)
                __ goal __ 0:
                    result.sort()
                    r_ result
    r_ None
