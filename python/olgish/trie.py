class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word):
        trie = {}
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
    
    def serach(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return None
        return trie # we exhausted the word ,that means we found it
