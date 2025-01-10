from math import floor, ceil
from heapq import heapify

class Solution:
    '''
        Constriants:
        - numbers of spells, potions: [1, e5]
        - values of spells, potions: [1, e5]
        - 1 <= success <= e10

        Comments/questions for interviewer
        - N/A

        Pseudo-code
        - loop through potions, find and track the minimum integer that is required to pass as successful in requirement
        - sort requirements using a min heap
        - loop through spells, and return value

        Analysis
        - 
    '''
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # populate requirements
        requirements = []
        for potion in potions:
            requirements.append(ceil(success/potion))
        
        # sort requirements
        requirements.sort()
        
        res = []
        for spell in spells:
            i = 0
            l = 0
            r = len(potions)
            
            # binary search requirements until same value is found
            while l < r:
                i = floor((r - l)/2) + l
                if requirements[i] <= spell:
                    l = i + 1
                else:
                    r = i
            res.append(l)
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.successfulPairs([5,1,3], [1,2,3,4,5], 7))
    print(s.successfulPairs([3,1,2], [8,5,8], 16))