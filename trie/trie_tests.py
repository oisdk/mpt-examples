from trie import *
import unittest
from random import randrange, choice
import re




with open('sherlock_holmes.txt') as file:
    words = set()
    for line in file:
        for word in re.split('\W+', line):
            words.add(word.strip().lower())
    words = list(words)

def rand_word(length):
    return choice(words)


def rand_words(length):
    return [rand_word(randrange(10)) for _ in range(length)]


class TrieTests(unittest.TestCase):
    def testInsertIsMember(self):
        for _ in range(100):
            t = Trie()
            words = rand_words(randrange(30))
            for word in words:
                t.add(word)
            for word in words:
                self.assertTrue(t.member(word))

    def testMakeTrie(self):
        for _ in range(100):
            words = rand_words(randrange(30))
            t = Trie.fromWords(*words)
            for word in words:
                self.assertTrue(t.member(word))

    def testIter(self):
        for _ in range(100):
            words = rand_words(randrange(30))
            t = Trie.fromWords(*words)
            l = [''.join(w) for w in sorted(set(words))]
            self.assertEqual(list(t),l)

    def testRemove(self):
        for _ in range(100):
            words = rand_words(randrange(30))
            word = rand_word(randrange(15))
            if not (word in words):
                t = Trie.fromWords(*words)
                tr = Trie.fromWords(*words)
                tr.add(word)
                tr.remove(word)
                self.assertEqual(t,tr)


if __name__ == '__main__':
    import doctest
    import trie
    doctest.testmod(m=trie)
    unittest.main()
