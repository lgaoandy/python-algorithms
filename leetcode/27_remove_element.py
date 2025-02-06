'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.

- Return k.
'''

class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        for x in nums.copy():
            if x != val:
                nums[i] = x
                i += 1
            else:
                nums[j] = "_"
                j -= 1
        return i


if __name__ == "__main__":
    test = Solution()
    nums1 = [3,2,2,3,2]
    print(test.remove_element(nums1, 3))
    print(nums1)

    nums2 = [0,1,2,2,3,0,4,2]
    print(test.remove_element(nums2, 2))
    print(nums2)