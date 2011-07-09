import Trie

trie = Trie.Trie('words.txt')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    """
    Generates all the words which have edit distance one with the
    given word
    """
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def spellcorrect(word):
    return dict((w, trie.find(w)) for w in edits1(word) if trie.find(w))

if __name__ == '__main__':
    print spellcorrect('accross')
