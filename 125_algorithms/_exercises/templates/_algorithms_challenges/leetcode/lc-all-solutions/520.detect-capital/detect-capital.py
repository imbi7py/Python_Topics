______ string


class Solution(object
  ___ detectCapitalUse(self, word
    """
    :type word: str
    :rtype: bool
    """
    ud = set(string.uppercase)
    ld = set(string.lowercase)
    n = le.(word)
    cap = 0
    for c in word:
      __ c in ud:
        cap += 1
    __ cap __ n:
      r_ True
    __ cap __ 1 and word[0] in ud:
      r_ True
    r_ False __ cap > 0 else True
