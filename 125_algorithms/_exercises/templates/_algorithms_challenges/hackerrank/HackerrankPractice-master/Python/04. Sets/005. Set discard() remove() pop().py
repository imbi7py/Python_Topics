# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Score: 10


n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    string = input().split()
    __ string[0] __ 'pop':
        s.pop()
    ____ string[0] __ 'remove':
        s.remove(int(string[1]))
    ____ string[0] __ 'discard':
        s.discard(int(string[1]))
print(sum(s))
