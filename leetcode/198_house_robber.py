from math import inf

class Solution:
    '''
        Intuition
        - Only constraint is you cannot rob two houses that are adjacent to each other
        - To max cash robbed, they will rob every other house
        - Therefore, there are only two real solutions, robbing odd or even houses
        
        Odd Even Approach [Failed]
        - Define variables even and odd
        - Iterate nums, adding the value of the index to odd or even based on the index
        - Return the greater value between even and odd
    '''
    def house_rob_odd_even(self, nums: list[int]) -> int:
        even, odd = 0, 0
        for i in range(len(nums)):
            if i % 2:
                odd += nums[i]
            else:
                even += nums[i]
        return max(even, odd)
    

    '''
        Dynamic Programming Approach
        - Define an array to track the sum of max amount of money to rob at the current starting from the left side
        - Define two pointers to hold index of the greatest value and the second greatest
        - Iterate through nums, populate the array and update pointers
        - Return the greater value between the last two values in the populated array
        - Time complexity: O(n) - iterates through nums once
        - Space complexity: O(n) - cash increases in size the same rate as nums, m1 & m2 - O(1)
    '''
    def house_rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        # if only one house exists:
        if n == 1:
            return nums[0]
        
        # initialize cash
        cash = nums[:2]

        # initialize greatest, m1, and second greatest, m2, values
        m1, m2 = 0, 1
        if nums[0] < nums[1]:
            m1, m2 = m2, m1
        
        # iterate the rest of nums
        for i in range(2, n):
            if m1 != i - 1: # if greatest is adjacent, take the second greatest
                cash.append(cash[m1] + nums[i])
                # shift greatest to current index, and second greatest to previous greatest
                m1, m2 = i, m1 
            else:
                cash.append(cash[m2] + nums[i])
                # update m1, m2 depends on whether current value is greater than the greatest value
                if cash[i] > cash[m1]:
                    m1, m2 = i, m1
                else:
                    m2 = i
        return max(cash[-2:])


if __name__ == "__main__":
    s = Solution()

    print(s.house_rob([1,2,3,1]))
    print(s.house_rob([2,7,9,3,1]))
    print(s.house_rob([5]))
    print(s.house_rob([2,1,1,2]))
    print(s.house_rob([101,100,1,1,1,5]))