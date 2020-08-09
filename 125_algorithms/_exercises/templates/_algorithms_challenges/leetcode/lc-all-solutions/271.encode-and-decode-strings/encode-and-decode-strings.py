class Codec:
  ___ encode(self, strs
    """Encodes a list of strings to a single string.
    
    :type strs: List[str]
    :rtype: str
    """
    ret = ""
    for s in strs:
      ret += str(le.(s)) + "|" + s

    r_ ret

  ___ decode(self, s
    """Decodes a single string to a list of strings.
    
    :type s: str
    :rtype: List[str]
    """
    ret = []
    start = end = 0
    w___ end < le.(s
      __ s[end] != "|":
        end += 1
      ____
        length = int(s[start:end])
        start = end + 1
        end = start + length
        ret.append(s[start:end])
        start = end
    r_ ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
