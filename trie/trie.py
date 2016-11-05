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

def makeTrie(*words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie
