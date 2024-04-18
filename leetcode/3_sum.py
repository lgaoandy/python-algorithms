'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

def three_sum(nums: list[int]) -> list[list[int]]:
    # use a dictionary to store triplets, only need the first two nums
    combinations = {}
    triplets = []

    # sort integer from smallest to largest
    nums.sort()

    # brute force
    for i in range(len(nums)):
        int1 = nums[i]
        for j in range(i+1, len(nums)-1):
            int2 = nums[j]
            for int3 in nums[j+1:]:
                if int1 + int2 + int3 == 0:
                    if int1 not in combinations.keys() or int2 not in combinations[int1]:
                        if int1 not in combinations.keys():
                            combinations[int1] = [int2]
                        else:
                            combinations[int1].append(int2)
                        triplets.append([int1, int2, int3])
    return triplets

if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0,1,1]))
    print(three_sum([0,0,0]))
