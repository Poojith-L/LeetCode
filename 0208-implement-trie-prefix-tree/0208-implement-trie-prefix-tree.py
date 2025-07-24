class Trie:

    def __init__(self):
        self.l=[]

    def insert(self, word: str) -> None:
        self.l.append(word)

    def search(self, word: str) -> bool:
        if word in self.l:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for w in self.l:
            if prefix in w:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)