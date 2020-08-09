"""
Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
__author__ = 'Danyang'
class Solution:
    digit2letters = {
        '2': "abc",
        '3': "___",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    ___ letterCombinations(self, digits
        """
        DFS
        :param digits: str
        :return: a list of strings, [s1, s2]
        """
        result = []
        self.dfs_traverse(digits, "", result)
        r_ result

    ___ dfs_traverse(self, string_seq, current, result
        __ not string_seq:
            result.append(current)
            r_

        for letter in self.digit2letters[string_seq[0]]:
            self.dfs_traverse(string_seq[1:], current+letter, result)


__ __name____"__main__":
    print Solution().letterCombinations("23")