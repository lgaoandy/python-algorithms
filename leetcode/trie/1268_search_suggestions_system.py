from string import ascii_lowercase

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False


    def insert(self, word: str):
        curr = self 
        for i in word:
            if i not in curr.children.keys():
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.isWord = True


    def search(self, word: str, k: int):
        curr = self
        for i in word:
            if i not in curr.children.keys():
                return []
            curr = curr.children[i]
        
        res = []
        def dfs(curr, chain):
            if len(res) == k:
                return
            
            if curr.isWord:
                res.append("".join(chain))
            
            for j in ascii_lowercase:
                if j in curr.children.keys():
                    chain.append(j)
                    dfs(curr.children[j], chain)
                    chain.pop()
                    
        dfs(curr, [i for i in word])
        return res


class Solution:
    def suggestedProductsTrie(self, products: list[str], searchWord: str) -> list[list[str]]:
        trie = Trie()

        for product in products:
            trie.insert(product)
        
        res = []
        for i in range(1, len(searchWord) + 1):
            res.append(trie.search(searchWord[0:i], 3))
        return res


    def suggestedProductsQuickSolution(self, products: list[str], searchWord: str) -> list[list[str]]:
        res = []
        products.sort()
        l, r = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):

                res[-1].append(products[l + j])
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
    print(s.suggestedProducts(["havana"], "havana"))
    print(s.suggestedProducts(["havana"], "tatiana"))