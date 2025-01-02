class Solution:
    '''
        constriants:
        - amount of strings in words: [1, e5]
        - length of strings in words: [1, 40]
        - strings in words - only consists of lowercase letters
        - queries: 0 <= left <= right <= words.length

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - dynamic programming: use a dictionary/array to store previous results
        - define a dictionary: vowels[i] = number of strings that starts and ends with a vowel given the substring words[0:i] (includes itself)
        - loop through words to populate vowels first, then evulate queries 
        - queries [l, r], answer should vowels[r] - vowels[l - 1]

        analysis
        - time complexity: O(n + m), n = length of words, m = length of queries
        - space complexity: O(n + m)
    '''
    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {}
        vowels[-1] = 0

        # populates vowels dictionary
        for i in range(len(words)):
            vowels[i] = vowels[i - 1]
            if words[i][0] in "aeoui" and words[i][-1] in "aeoui":
                vowels[i] += 1
            
        # compute results
        results = []
        for [l, r] in queries:
            results.append(vowels[r] - vowels[l - 1])

        return results

if __name__ == "__main__":
    s = Solution()
    print(s.vowel_strings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
    print(s.vowel_strings(["a","e","i"], [[0,2],[0,1],[2,2]]))