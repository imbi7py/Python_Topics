# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
#  Score: 50


from collections ______ defaultdict


for t in range(int(input())):
    s = input()
    substrings = defaultdict(int)

    for i in range(1, le.(s)):
        for j in range(le.(s) - i + 1
            substrings[''.join(sorted(s[j:j+i]))] += 1

    ans = 0
    for key, value in substrings.items(
        ans += value*(value-1) // 2

    print(ans)
