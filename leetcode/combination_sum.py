'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

import math

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # sort candidates from least to greatest
    candidates.sort()
    results = []

    for i in range(len(candidates)):
        if candidates[i] == target:  # if num is target, add to solution and break since nums left in sequence will not provide any solution
            results.append([candidates[i]])
            break
        else: # if not, num is smaller than target
            solution = []
            multiple = math.ceil(target / candidates[i]) # find greatest multiple

            while multiple > 0:
                if multiple * candidates[i] == target: # check if this current multiple is a solution
                    solution = [candidates[i]] * multiple
                else: # find other possible combinations
                    if ()

                # save solution if available
                if len(solution) > 0:
                    results.append(solution)
                multiple -= 1

            

            
        # num smaller than target
            # find the biggest multiple of the current num
            # while loop, try to fit a solution each multiple of the num - other nums that are higher can be used but not lower
                # 7: [2, 2, 2, 2, 2, 2, 2]
                # 6: no solution
                # 5: [2, 2, 2, 2, 2, 4]
                # 4: [2, 2, 2, 2, 3 ,3]
                # 3: [2, 2, 2, 4, 4]
                # 2: [2, 3, 3, 4]
                # 1: [2, 4, 4, 4] and [2, 3, 3, 3, 3]
    
    return results


if __name__ == "__main__":
    print(combination_sum([2, 3, 4], 14))