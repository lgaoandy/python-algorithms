class Solution:
    '''
        comments/questions for interviewer
        - N/A

        pseudo-code
        - loop words, using startsWith(), if true, add to count, return count end of func

        analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count
    

if __name__ == "__main__":
    s = Solution()
    print(s.prefixCount(["pay","attention","practice","attend"], "at"))
    print(s.prefixCount(["leetcode","win","loops","success"], "code"))