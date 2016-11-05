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
        `word` is in the trie `self`.

        >>> t = Trie()
        >>> t.member("abc")
        False
        >>> t.add("abc")
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

    def add(self, word):
        """
        adds the sequence `word` into `self`.

        >>> t = Trie()
        >>> print(t)
        []
        >>> t.add("abc")
        >>> print(t)
        ['abc']
        """
        current = self
        for letter in word:
            current = current._children.setdefault(letter, Trie())
        current._endsHere = True

########################################################################
# That's all that was covered on Saturday, below here is stuff you
# might want to try implementing yourself before you have a look at it.
# If you're stuck, though, feel free to use it!

    def suffixes(self, word):
        """
        Returns a trie of the suffixes of `word` in `self`.

        >>> t = Trie.fromWords("carpet", "carpark")
        >>> t.suffixes("car")
        ['park', 'pet']
        """
        result = self
        for letter in word:
            try:
                result = result._children[letter]
            except KeyError:
                return Trie()
        return result

    def remove(self, word):
        self._remove(iter(word))

    def _remove(self, word_iter):
        """Internal method for removing a word from the trie. If the
        word isn't present, it will raise a KeyError.

        It also returns a bool, to optimize space. Consider, for
        instance, the trie of ["car", "carpet"]:

        c-a-r.p-e-t.

        To delete "car", the tag on 'r' can just be flipped:

        c-a-r-p-e-t.

        To delete "carpet" and keep "car", the tag on 't' must be
        flipped:

        c-a-r.p-e-t

        But now the p-e-t is being stored unnecessarily.

        For this reason, the function returns a bool, which means
        "delete me!" when True, or "keep me!" when False.
        """
        try:
            head = next(word_iter)
            chld = self._children[head]
            if chld._remove(word_iter):
                del self._children[head]
        except StopIteration:
            self._endsHere = False
        return not (self._endsHere or self._children)

    def __len__(self):
        return sum(map(len, self._children.values())) + self._endsHere


########################################################################
# Below here is stuff not necessary for the algorithm, just useful for
# debugging, etc.

    def discard(self, word):
        try: self.remove(word)
        except KeyError: pass

    def __contains__(self, word):
        return self.member(word)

    def fromWords(*words):
        """
        Creates a trie from several words.

        >>> Trie.fromWords("abc", "def")
        ['abc', 'def']
        >>> Trie.fromWords([1,2,3],[4,5,6])
        [[1, 2, 3], [4, 5, 6]]
        """
        trie = Trie()
        for word in words:
            trie.add(word)
        return trie

    def _values(self, prefix):
        """Helper function to allow iteration"""
        if self._endsHere:
            yield prefix
        is_str = type(prefix) is str
        for head, child in sorted(self._children.items()):
            if is_str and type(head) is str:
                next_prefix = prefix + head
            else:
                next_prefix = list(prefix) + [head]
            yield from child._values(next_prefix)

    def __eq__(self, other):
        return self._endsHere == other._endsHere and self._children == other._children

    def __iter__(self):
        return self._values("")

    def __repr__(self):
        return list(self).__repr__()

    def __str__(self):
        return str(list(self))

    def _debug_view(self, size, pad, first=False):


        if first:
            wspaces = [('','')] * len(self._children)
            npad = ''
        else:
            yield '.' if self._endsHere else '─'
            npad = pad + '{0:>{width}}'.format('│ ', width=size+1)
            wspaces  = [('',npad)]
            wspaces += [(pad + '{0:>{width}}'.format('├─', width=size+1),npad)
                        for _ in range(len(self._children)-2)]
            if len(self._children) > 1:
                wspaces += [(pad + '{0:>{width}}'.format('└─', width=size+1),
                             npad)]
            wspaces[-1] = (wspaces[-1][0], pad + (' ' * (size+1)))
        it_by_len = sorted(self._children.items())
        for (wspace,npad), (head, child) in zip(wspaces, it_by_len):
            yield wspace
            yield '{0:>{width}}'.format(head, width=size)
            yield from child._debug_view(size, npad)
        if not self._children:
            yield '\n'

    def letters(self):
        for head, child in self._children.items():
            yield head
            yield from child.letters()

    def debug_view(self):
        s = max((len(str(l)) for l in self.letters()), default=0)
        view = self._debug_view(s, 0, True)
        return ''.join(view)

def complete():
    import re
    with open('sherlock_holmes.txt') as file:
        trie = Trie()
        for line in file:
            for word in re.split('\W+', line):
                trie.add(word.lower())
        print('type a word to see its suffixes. q to quit.')
        for line in iter(input, 'q'):
            word = line.strip().lower()
            for suff in trie.suffixes(word):
                print(word + suff)
            print()

def build():
    trie = Trie()
    print('type in a word to add it to the trie. q to quit.')
    for line in iter(input, 'q'):
        print()
        trie.add(line.strip().lower())
        print(trie.debug_view())

if __name__ == '__main__':
    complete()
    build()
