class Trie:
    def __init__(self):
        self._endsHere, self._children = False, {}

    def member(self, word):
        current = self
        for letter in word:
            try:
                current = current._children[letter]
            except KeyError:
                return False
        return current._endsHere

    def insert(self, word):
        current = self
        for letter in word:
            current = current._children.setdefault(letter, Trie())
        current._endsHere = True

    def _values(self, prefix):
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



def makeTrie(*words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie
