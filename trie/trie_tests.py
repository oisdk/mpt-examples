from trie import *
import unittest
from random import randrange


def rand_tuple(length):
    return tuple(randrange(30) for _ in range(30))


def rand_tuples(length):
    return [rand_tuple(randrange(10)) for _ in range(length)]


class TrieTests(unittest.TestCase):
    def testInsertIsMember(self):
        for _ in range(100):
            t = Trie()
            words = rand_tuples(randrange(30))
            for word in words:
                t.insert(word)
            for word in words:
                self.assertTrue(t.member(word))

    def testMakeTrie(self):
        for _ in range(100):
            words = rand_tuples(randrange(30))
            t = makeTrie(*words)
            for word in words:
                self.assertTrue(t.member(word))

    def testIter(self):
        for _ in range(100):
            words = rand_tuples(randrange(30))
            t = makeTrie(*words)
            l = sorted(map(list, set(words)))
            self.assertEqual(list(t),l)


if __name__ == '__main__':
    unittest.main()
