# Problem: https://www.hackerrank.com/challenges/counting-valleys/problem
#  Score: 15


___ counting_valleys(n, s
    current_level = 0
    count = 0
    for i in range(n
        __ s[i] __ 'U':
            current_level += 1
        ____ s[i] __ 'D':
            current_level -= 1
            __ current_level __ -1:
                count += 1
    r_ count


n = int(input().strip())
s = input().strip()
result = counting_valleys(n, s)
print(result)
