import Trie

trie = Trie.Trie('words.txt')
trie.insert('accord')

def suggest(prefix):
    words = trie.wordsWithPrefix(prefix, True)
    print words
    return sorted(words, key = words.get, reverse = True)

if __name__ == '__main__':
    print suggest('acc')
