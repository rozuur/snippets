
import Trie

trie = Trie.Trie('words.txt')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    """
    Generates all the words which have edit distance one with the
    given word
    """
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    # delete a character in word [sample] -> [ample],[smple],[saple]..
    deletes    = [a + b[1:] for a, b in splits if b]
    # transposes one character with its neighbour -> [asmple], [smaple]..
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    # replace once character in word with some other alphabet
    # sample ->aample, bample, cample ..., sbmple, scmple,...
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    # insert an extra character in word
    # sample -> asample, bsample,..., saample, sbample,...
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def spellcorrect(word):
    return dict((w, trie.find(w)) for w in edits1(word) if trie.find(w))

if __name__ == '__main__':
    print "Correct spelling for 'accross' is ",
    print spellcorrect('accross').keys()[0]
