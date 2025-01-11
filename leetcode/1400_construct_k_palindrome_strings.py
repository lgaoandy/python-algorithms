from collections import Counter

class Solution:
    '''
        Constriants:
        - consists for only lowercase letters

        Comments/questions for interviewer
        - N/A

        Analysis
        - time complexity: O()
    '''
    def canConstruct(self, s: str, k: int) -> bool:
        occurrences = { i:0 for i in set(s) }
        for i in s:
            occurrences[i] += 1

        odd = set()
        value = 0
        for i in occurrences.keys():
            if occurrences[i] % 2:
                odd.add(i)
            value += occurrences[i]
        if len(odd) > k:
            return False
        return value >= k
    
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(c%2 for c in Counter(s).values()) <= k <= len(s)
        

if __name__ == "__main__":
    s = Solution()

    print(s.canConstruct("annabelle", 2)) # true
    print(s.canConstruct("leetcode", 3)) # false
    print(s.canConstruct("true", 4)) # true
    print(s.canConstruct("aaa", 2)) # true