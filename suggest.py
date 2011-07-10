
import Trie

# initialize trie with a file
# for best results use text from a novel or book so as to include
# frequency of normal occurrence of word
trie = Trie.Trie('words.txt')

# since we are inserting accord second time
# it will be suggested first
trie.insert('accord')

def suggest(prefix):
    """
    returns a list of words with prefix
    """
    # returns all the words with prefix including its insertion count
    words = trie.wordsWithPrefix(prefix, True)
    # sort words based on its frequency
    return sorted(words, key = words.get, reverse = True)

if __name__ == '__main__':
    print "Words starting with prefix 'acc'",
    print suggest('acc')
