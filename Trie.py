class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = {} # stores child nodes
        self.freq = 0 # frequenc of word
        if parent:
            parent.children[value] = self

    def isWord(self):
        return self.freq != 0

    def __str__(self):
        return '<Trie Node having children %d>'%len(self.children)
    
class Trie:
    def __init__(self, inputfile = None):
        self.root = TrieNode(None, '')
        if inputfile:
            self._addWordsFromFile(inputfile)
        
    def _addWordsFromFile(self, inputfile):
        with open(inputfile, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    self.insert(word)
    
    def insert(self, word):
        word = word.strip().lower() # stores all words in lower
        if not word: 
            return
        current = self.root
        for c in word: 
            if c in current.children: # if char c is in children nodes
                current = current.children[c] # update current node
            else:
                current = TrieNode(current, c) # or create a new node and add c
        current.freq += 1 # update no of times word is inserted

    def find(self, word):
        """
        returns no of times word is inserted into Trie
        """
        word = word.strip().lower()
        current = self.root
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                return False
        return current.freq
    
    def _allwords(self, node, prefix):
        """
        recursively finds all words starting with prefix
        returns a dictionary of words and frequency
        """
        words = {}
        for char, child in node.children.items():
            if child.isWord(): 
                words[prefix + char] = child.freq
            words.update(self._allwords(child, prefix + char))
        return words

    def wordsWithPrefix(self, prefix, includeFrequency = False):
        """
        based on includeFrequency returns a list or dictionary of words
        starting with prefix
        """
        prefix = prefix.strip().lower()
        if not prefix:
            return
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return [] # prefix is not present in trie 
        words = self._allwords(current, prefix)
        if includeFrequency:
            return words
        else:
            return words.keys()
        
    def _charfmt(self, c):
        return '--[{0}]'.format(c)

    def _display(self, node, depth, fmt):
        """
        recursively displays each word
        """
        childs = node.children.keys()
        if not childs: 
            return
        tabs = '   '
        for c in childs[:-1]:
            print fmt + '|' +  self._charfmt(c)
            self._display(node.children[c], 0, fmt + '|' + tabs)
        # last child is displayed by a backslash to mark ending    
        print fmt + '\\'  + self._charfmt(childs[-1])
        self._display(node.children[childs[-1]], 0, fmt + ' ' + tabs)


    def display(self):
        print '[-]'
        self._display(self.root, 0, ' ')

if __name__ == '__main__':
    tr = Trie('words.txt')
    print 'Displaying Trie'
    tr.display()
    print
    print 'Is "across" in Trie',
    print tr.find('across') != 0
    print 'Words with prefix "acc"',
    print tr.wordsWithPrefix('acc')
    
