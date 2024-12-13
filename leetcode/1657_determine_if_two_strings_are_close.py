from collections import Counter

class Solution:
    '''
        understanding the problem
        - on initial look, problem may seem complicated as operation 1 & 2 can be done in any order and any number of times
        - let's take a look for each operation:
            - operation 1 
                - close words can be any form of anagrams, or in other words:
                - same set of chars is required but position do not matter
            - operation 2
                - the number of occurrences of different chars must be the same
                - however, the char of which occurrence is assigned to, do not
        - therefore, in our function, we must check for closeness:
            - words must have the same length
            - words must have the same set of unique chars
            - words must have the same list of occurrences unattached to specific chars

        pseudo-code
        - if word lengths differ, return FALSE
        - convert both words into set, if set is not the same, return FALSE
        - count the number of occurrence of each char in each word, return FALSE if the list is not the same
        - return TRUE in all other cases
    '''
    def close_strings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        occurrences1 = Counter(word1).values()
        occurrences2 = Counter(word2).values()
        return Counter(occurrences1) == Counter(occurrences2)

if __name__ == "__main__":
    test = Solution()
    print(test.close_strings("abc", "bca"))
    print(test.close_strings("a", "aa"))
    print(test.close_strings("cabbba", "abbccc"))