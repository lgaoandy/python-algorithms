class Solution:
    '''
        constriants:
        - 1 <= words <= 50
        - 1 <= length of words <= 10
        - only lowercase letters

        comments/questions for interviewer
        - N/A

        pseudo-code
        - check for left to right
        - a word does not need to check if a word that is smaller than itself

        analysis
        - time complexity: O(nlogn)
        - space complexity: O(1)
    '''
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        n = len(words)
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            return str2.find(str1) == 0 and str2.rfind(str1) == len(str2) - len(str1)

        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
    

if __name__ == "__main__":
    s = Solution()

    print(s.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
    print(s.countPrefixSuffixPairs(["pa","papa","ma","mama"]))
    print(s.countPrefixSuffixPairs(["abab","ab"]))