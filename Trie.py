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

    def charfmt(self, c):
        return '--[{0}]'.format(c)

    def _display(self, node, depth, fmt):
        childs = node.children.keys()
        if not childs: 
            return
        for c in childs[:-1]:
            print fmt + '|' +  self.charfmt(c)
            self._display(node.children[c], 0, fmt + '|   ')
        print fmt + '+'  + self.charfmt(childs[-1])
        self._display(node.children[childs[-1]], 0, fmt + '   ')


    def display(self):
        print '[-]'
        self._display(self.root, 0, ' ')
            

"""
[-]
 |--[A]
 |--[T]
 |   |--[E]
 |       |--[A]
 |       |   |--[A]
 |       |--[D]
 |       |--[N]
 |--[I]
     |--[N]
         |--[N]
"""

"""
[-]
 |--[A]
 |--[T]
 |   +--[E]
 |       |--[A]
 |       |   +--[A]
 |       |--[D]
 |       +--[N]
 +--[I]
     +--[N]
         +--[N]
"""

if __name__ == '__main__':
    tr = Trie()
    words = ["A", "to", "tea", "ted", "ten", "i", "in",  "inn"]
    #words = ["to", "tea", "ted", "ten",]
    for word in words:
        tr.insert(word)
    tr.display()
    
