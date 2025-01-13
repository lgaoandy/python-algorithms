class Solution:
    '''
        Constriants:
        - length of string: [1, 2e5]
        - only consists of lowercase letters

        Comments/questions for interviewer
        - count occurrences of each letter going through string
        - trim any letters with 3 or more

        Pseudo-code
        - if greater than 3 and odd, return 1
        - if greater than 3 and even, return 2

        Analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def minimumLength(self, s: str) -> int:
        letters = { i:0 for i in set(s) }
        for i in s:
            letters[i] += 1
        
        count = 0
        for i in letters.keys():
            count += 1 if letters[i] % 2 else 2
        return count


if __name__ == "__main__":
    s = Solution()
    
    print(s.minimumLength("abaacbcbb"))
    print(s.minimumLength("aa"))
    print(s.minimumLength("lyqkwhyy"))