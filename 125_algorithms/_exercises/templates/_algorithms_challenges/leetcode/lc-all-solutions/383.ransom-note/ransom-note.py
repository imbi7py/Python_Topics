class Solution(object
  ___ canConstruct(self, ransomNote, magazine
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    letters = [0] * 26
    for c in magazine:
      letters[ord(c) - ord('a')] += 1

    for c in ransomNote:
      __ letters[ord(c) - ord('a')] __ 0:
        r_ False
      ____
        letters[ord(c) - ord('a')] -= 1
    r_ True
