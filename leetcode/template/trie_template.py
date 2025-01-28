class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        curr = self
        n = len(word)

        for i in range(n):
            letter = word[i]
            if letter not in curr.children.keys():
                curr.children[letter] = Trie()
            curr = curr.children[letter]
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self
        
        for letter in word:
            if letter not in curr.children.keys():
                return False
            curr = curr.children[letter]
        return curr.isWord
    

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for letter in prefix:
            if letter not in curr.children.keys():
                return False
            curr = curr.children[letter]
        return True
