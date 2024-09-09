class Solution():
    '''
        Pseudo-code
        - use 2 pointers, one in s, one in t
        - loop both arrays at the same time
        - if end of s is reached first, return true, else false
    '''
    def is_subsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while True:
            if s_index > len(s):
                return True
            if t_index > len(t):
                return False
            if t[t_index] == s[s_index]:
                s_index += 1
            t_index += 1

if __name__ == "__main__":
    test = Solution()
    print(test.is_subsequence_brute_force("abc", "ahbgdc"))
    print(test.is_subsequence_brute_force("axc", "ahbgdc"))
    print(test.is_subsequence_brute_force("ace", "aec"))