class TrieNode:
    ___ __init__(self, val=None
        self.end_at = val
        self.children = {}


class Trie:
    ___ __init__(self
        self.trie = TrieNode()

    ___ insert(self, word
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        __ not word:
            r_

        node = self.trie
        for char in word:
            __ char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_at = word

    ___ search(self, word
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        __ not word:
            r_ False

        node = self.trie
        for char in word:
            __ char not in node.children:
                r_ False
            node = node.children[char]
        r_ node.end_at __ word

    ___ startsWith(self, prefix
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        __ not prefix:
            r_ False

        node = self.trie
        for char in prefix:
            __ char not in node.children:
                r_ False
            node = node.children[char]
        r_ True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
