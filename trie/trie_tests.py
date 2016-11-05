from trie import *
import unittest
from random import randrange


def rand_list(length):
    return [randrange(30) for _ in range(30)]


def rand_lists(length):
    return [rand_list(randrange(10)) for _ in range(length)]


class TrieTests(unittest.TestCase):
    def testInsertIsMember(self):
        for _ in range(100):
            t = Trie()
            words = rand_lists(randrange(30))
            for word in words:
                t.insert(word)
            for word in words:
                self.assertTrue(t.member(word))

    def testMakeTrie(self):
        for _ in range(100):
            words = rand_lists(randrange(30))
            t = makeTrie(*words)
            for word in words:
                self.assertTrue(t.member(word))


if __name__ == '__main__':
    unittest.main()
