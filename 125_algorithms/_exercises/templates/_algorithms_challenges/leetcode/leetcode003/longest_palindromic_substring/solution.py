class Solution:
    # @return a string
    ___ longestPalindrome(self, s
        n = le.(s)
        t = [[False for i in range(n)] for j in range(n)]
        start = 0
        max_len = 1
        for i in range(n
            t[i][i] = True
        for i in range(n - 1
            j = i + 1
            __ s[i] __ s[j]:
                t[i][j] = True
                start = i
                max_len = 2
        for l in range(3, n + 1
            for i in range(n - l + 1
                j = i + l - 1
                __ s[i] __ s[j] and t[i + 1][j - 1]:
                    t[i][j] = True
                    start = i
                    max_len = l
        r_ s[start:start + max_len]


a = 'akaa2baakcbbc'
s = Solution()
print s.longestPalindrome(a)
