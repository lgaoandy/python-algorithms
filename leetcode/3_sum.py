'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

# brute force method
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

# efficent method
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)

    # given one number, need to find two other numbers in the list that cancels it
    for i in range(n - 2):
        # solution will be same of the same value
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1 # start on leftmost next of i
        right = n - 1 # start on rightmost end
        print(left, right)

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # ensure the next leftmost num is not the same number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([0,1,1]))
    print(three_sum([0,0,0]))
