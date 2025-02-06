class Solution:
    '''
        Intuition
        - Given two string, if there are more than two positions where the char differs from each other, it is false
    '''
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap.append(i)
        
        n = len(swap)
        if n > 2 or n % 2 != 0:
            return False
        if n == 0:
            return True
        return s1[swap[0]] == s2[swap[1]] and s1[swap[1]] == s2[swap[0]]


if __name__ == "__main__":
    s = Solution()
    print(s.areAlmostEqual("bank", "kanb"))
    print(s.areAlmostEqual("attack", "defend"))
    print(s.areAlmostEqual("kelb", "kelb"))
    print(s.areAlmostEqual("ac", "aa"))
    print(s.areAlmostEqual("caa", "aaz"))