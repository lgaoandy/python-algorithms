from collections import defaultdict

class Solution:
    '''
        constriants:
        - 3 <= s.length <= e5
        - s consists only lowercase letters

        comments/questions for interviewer
        - N/A

        pseudo-code
        - First pass through: make 2 dictionaries
        - One dictionary keeps track of each letter's first and last occurrences, saved their indexes
        - using both dictionaries, we can derive a count

        analysis
        - time complexity: O(n)
        - space complexity: O(n)
    '''
    def countPalindromicSubsequence(self, s: str) -> int:
        occurrences = { i:[] for i in set(s) }
        
        # populate occurrences
        for i in range(len(s)):
            occurrences[s[i]].append(i)
        
        # every letter with more than 2 occurrences has a chance to have unique palindromes
        count = 0
        for i in occurrences.keys():
            if len(occurrences[i]) >= 2:
                start = occurrences[i][0]
                end = occurrences[i][-1]
                
                # check every unique letter that exists in between the start and end indexes
                for indexes in occurrences.values():
                    if any(start < num < end for num in indexes):
                        count += 1
        return count
    
    
    '''
        comments
        - utilizes .find(), and rfind() to get ocurrences
        - utilizes set to find unique letters for counting subsequences
        - time complexity: O(1)
        - space complexity: O(1)
    '''
    def countPalindromicSubsequence_optimized(self, s: str) -> int:
        count = 0
        for char in set(s): # iterates over unique characters
            i, j = s.find(char), s.rfind(char) # get first and last occurrences
            if j > i + 1: # ensures there's at least two occurrences
                char += len(set(s[i+i:j]))
        return count
    

if __name__ == "__main__":
    s = Solution()
    print(s.countPalindromicSubsequence("aabca")) # expected 3
    print(s.countPalindromicSubsequence("adc")) # expected 0
    print(s.countPalindromicSubsequence("bbcbaba")) # expected 4