class Trie:
    def __init__(self):
        self.children = set()
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass

if __name__ == "__main__":

    trie = Trie()
    trie.insert("apple")
    trie.search("apple")    # return True
    trie.search("app")      # return False
    trie.startsWith("app")  # return True
    trie.insert("app")
    trie.search("app")      # return True