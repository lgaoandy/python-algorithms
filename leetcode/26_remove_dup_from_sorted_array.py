class Solution:
    def removeDuplicatesWithSet(self, nums: list[int]) -> int:
        seen = set()
        i = 0
        for num in nums.copy():
            if num not in seen:
                nums[i] = num
                seen.add(num)
                i += 1
        return i


    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        for num in nums.copy():
            if num != nums[i-1]:
                nums[i] = num
                i += 1
        return i


if __name__ == "__main__":
    s = Solution()

    nums1 = [1,1,2]
    k = s.removeDuplicates(nums1)
    print(k)
    print(nums1[0:k])

    nums1 = [0,0,1,1,1,2,2,3,3,4]
    k = s.removeDuplicates(nums1)
    print(k)
    print(nums1[0:k])