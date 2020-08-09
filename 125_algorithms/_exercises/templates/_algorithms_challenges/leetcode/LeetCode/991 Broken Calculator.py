#!/usr/bin/python3
"""
On a broken calculator that has a number showing on its display, we can perform
two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.



Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.


Note:

1 <= X <= 10^9
1 <= Y <= 10^9
"""


class Solution:
    ___ brokenCalc(self, X: int, Y: int) -> int:
        """
        greedy + work backward

        If Y is odd, we can do only Y = Y + 1
        If Y is even, if we plus 1 to Y, then Y is odd, we need to plus another 1.
        And because (Y + 1 + 1) / 2 = (Y / 2) + 1, 3 operations are more than 2.
        We always choose Y / 2 if Y is even.
        """
        t = 0
        w___ Y > X:
            __ Y % 2 __ 0:
                Y //= 2
            ____
                Y += 1
            t += 1

        r_ t + X - Y

    ___ brokenCalc_TLE(self, X: int, Y: int) -> int:
        """
        BFS
        """
        q = [X]
        t = 0
        has_larger = False
        w___ q:
            cur_q = []
            for e in q:
                __ e __ Y:
                    r_ t

                cur = e * 2
                __ cur >= 1:
                    __ cur > Y and not has_larger:
                        has_larger = True
                        cur_q.append(cur)
                    ____ cur <= Y:
                        cur_q.append(cur)

                cur = e - 1
                __ cur >= 1:
                    cur_q.append(cur)
            q = cur_q
            t += 1

        raise


__ __name__ __ "__main__":
    assert Solution().brokenCalc(2, 3) __ 2
