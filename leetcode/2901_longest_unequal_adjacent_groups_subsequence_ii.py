class Solution:
    '''
        Dynamic Programming
        - build the solution piece by piece
        
        dp[i] = length of longest valid subsequence ending with words[i]
        prev[i] = index of the word before words[i] in that subsequence
        
        if words[j] can precede words[i] (rules met)
        dp[i] = max(dp[i], dp[j]+1)
    '''
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[str]) -> list[str]:
        n = len(words)
        
        if n == 0:
            return []
        
        dp = [1] * n
        prev = [-1] * n
        
        def hamming_distance(s1, s2):
            count = 0
            for char1, char2 in zip(s1, s2):
                if char1 != char2:
                    count += 1
            return count
        
        max_len = 1
        end_idx = 0
        
        for i in range(n):
            # dp[i] is already 1, prev[i] is -1
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j
                
            # after checking all j's for current i, update overall max_len
            if dp[i] > max_len:
                max_len = dp[i]
                end_idx = i
                
        # reconstruct the subsequence
        result = []
        curr = end_idx
        while curr != -1:
            result.append(words[curr])
            curr = prev[curr]
        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    
    words = ["bab", "dab", "cab"]
    group = [1,2,2]
    print(s.getWordsInLongestSubsequence(words, group))
    
    words = ["a", "b", "c", "d"]
    group = [1,2,3,4]
    print(s.getWordsInLongestSubsequence(words, group))
    
    words = ["sap", "sip", "tup", "fup"]
    group = [1,2,3,4]
    print(s.getWordsInLongestSubsequence(words, group))