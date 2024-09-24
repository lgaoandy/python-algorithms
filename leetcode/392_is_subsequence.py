class Solution:
    '''
        Pseudo-code
        - use 2 pointers, one in s, one in t
        - loop both arrays at the same time
        - if end of s is reached first, return true, else false
    '''
    def is_subsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while t_index < len(t) and s_index < len(s):
            if t[t_index] == s[s_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)

if __name__ == "__main__":
    test = Solution()
    print(test.is_subsequence("abc", "ahbgdc"))
    print(test.is_subsequence("axc", "ahbgdc"))
    print(test.is_subsequence("ace", "aec"))