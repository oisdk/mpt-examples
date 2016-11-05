class Trie:
    def __init__(self):
        """
        Initialises an empty trie

        >>> Trie()
        []
        """

        self._endsHere, self._children = False, {}

    def member(self, word):
        """
        Returns a bool representing whether or not the sequence
        `word` is in the trie `self`

        >>> t = Trie()
        >>> t.member("abc")
        False
        >>> t.insert("abc")
        >>> t.member("abc")
        True
        """
        current = self
        for letter in word:
            try:
                current = current._children[letter]
            except KeyError:
                return False
        return current._endsHere

    def insert(self, word):
        """
        inserts the sequence `word` into `self`

        >>> t = Trie()
        >>> print(t)
        []
        >>> t.insert("abc")
        >>> print(t)
        [['a', 'b', 'c']]
        """
        current = self
        for letter in word:
            current = current._children.setdefault(letter, Trie())
        current._endsHere = True

########################################################################
# Below here is stuff not necessary for the algorithm, just useful for
# debugging, etc.

    def fromWords(*words):
        """
        Creates a trie from several words.

        >>> Trie.fromWords("abc", "def")
        [['a', 'b', 'c'], ['d', 'e', 'f']]
        >>> Trie.fromWords([1,2,3],[4,5,6])
        [[1, 2, 3], [4, 5, 6]]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie

    def _values(self, prefix):
        """Helper function to allow iteration"""
        if self._endsHere:
            yield prefix
        for head, child in sorted(self._children.items()):
            yield from child._values(prefix + [head])

    def __iter__(self):
        return self._values([])

    def __repr__(self):
        return list(self).__repr__()

    def __str__(self):
        return str(list(self))
