class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = {}
        self.isWord = False
        if parent:
            parent.children[value] = self
            
    def __str__(self):
        return '<Trie Node having children {0}>'\
            .format(''.join(self.children))
    
class Trie:
    def __init__(self):
        self.root = TrieNode(None, '')
    
    def insert(self, word):
        word = word.strip()
        if not word: 
            return
        current = self.root
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                current = TrieNode(current, w)
        current.isWord = True

    def find(self, word):
        word = word.strip()
        current = self.root
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                return False
        return current.isWord

    def display(self):
        print 'root = ', self.root
        for c in self.root.children:
            print c, self.root.children[c]


if __name__ == '__main__':
    tr = Trie()
    for word in ["A", "to", "tea", "ted", "ten", "i", "in",  "inn"]:
        tr.insert(word)
    tr.display()
    
