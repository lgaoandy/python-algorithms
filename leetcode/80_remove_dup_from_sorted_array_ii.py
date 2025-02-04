class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-1] or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i
    

if __name__ == "__main__":
    s = Solution()

    nums1 = [1,1,1,2,2,3]
    k = s.removeDuplicates(nums1)
    print(k)
    print(nums1[0:k])

    nums1 = [0,0,1,1,1,1,2,3,3]
    k = s.removeDuplicates(nums1)
    print(k)
    print(nums1[0:k])

    nums1 = [0,0]
    k = s.removeDuplicates(nums1)
    print(k)
    print(nums1[0:k])