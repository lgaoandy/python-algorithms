import math

class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        # identify base case as a patch insisting ONLY of empty spaces
        # input n = number of spaces, outputs number of flower planted
        def can_place_flowers_in_empty_spaces(x: int) -> int:
            if x > 0:
                return math.ceil(x/2)
            else:
                return 0

        # loop flowerbed, identifing all empty patches by tracking the last non-empty space
        # until end of loop or when another empty space is found
        flowers = 0
        prev_non_empty = -1
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                # case 11
                if prev_non_empty != -1:
                    flowers += can_place_flowers_in_empty_spaces(i - prev_non_empty - 3)
                # case 01
                else:
                    flowers += can_place_flowers_in_empty_spaces(i - 1)
                prev_non_empty = i
            elif i + 1 == len(flowerbed):
                # case 10
                if prev_non_empty != -1:
                    flowers += can_place_flowers_in_empty_spaces(i - prev_non_empty - 1)
                # case 00
                else:
                    flowers += can_place_flowers_in_empty_spaces(i + 1)
        
        # evaluate total flowers
        return flowers >= n
    
    '''
        Weaknesses from PHIND
        1) logic of handling different cases can be simplified
        2) variable names could be more descriptive
        3) solution uses a new variable to track flowers rather than using n
    '''
    def can_place_flowers_optimized(self, flowerbed: list[int], n: int) -> bool:
        # copy flowerbed to prevent function from being impure
        flowerpatch = flowerbed.copy()
        
        if n == 0:
            return True
        for i in range(len(flowerpatch)):
            # focuses only on cases where flowers can be planted
            if flowerpatch[i] == 0 and (i == 0 or flowerpatch[i-1] == 0) and (i == len(flowerpatch)-1 or flowerpatch[i+1] == 0):
                # takes a real time approach, when a flower is counted, flowerbed is updated to prevent double counting
                flowerpatch[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.can_place_flowers([1,0,0,0,1], 1))
    print(solution.can_place_flowers([1,0,0,0,1], 2))
    print(solution.can_place_flowers([1,0,1,0,1,0,1], 1))
    print(solution.can_place_flowers([0,0,1,0,1], 1))
    print(solution.can_place_flowers([0,1,0,], 1))
    print(solution.can_place_flowers([1,0,0,0,1,0,0], 2))

    flowerbed1 = [1,0,0,0,1,0,0]
    print(solution.can_place_flowers_optimized(flowerbed1, 2))
    print(flowerbed1)

# What I learned
# - when solving a problem, if you need to obtain bonus info in the process, there's a better way
# - simplifying a problem is key
# - if a function modifies an array or object, make a copy of it in the start of the function