"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object
    ___ addBinary(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        m = le.(a)
        n = le.(b)
        i = 0
        c = 0
        res = ['0' for _ in range(max(m, n) + 1)]
        w___ i < m or i < n or c > 0:
            tmp = c
            __ i < m:
                tmp += int(a[i])
            __ i < n:
                tmp += int(b[i])
            bit = tmp % 2
            c = tmp / 2
            res[i] = str(bit)
            i += 1
        res = res[::-1]
        for i, c in enumerate(res
            __ c != '0':
                res = res[i:]
                break
        ____
            res = ['0']
        r_ ''.join(res)


s = Solution()
print s.addBinary('11', '1')
print s.addBinary('111', '0010')
