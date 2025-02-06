class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[0:m]
        i = 0
        j = 0

        while i < m and j < n:
            if nums3[i] <= nums2[j]:
                nums1[i+j] = nums3[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        
        while j < n:
            nums1[i+j] = nums2[j]
            j += 1
        while i < m:
            nums1[i+j] = nums3[i]
            i += 1
        


if __name__ == "__main__":
    s = Solution()

    nums1 = [1,2,3,0,0,0]
    s.merge(nums1, 3, [2,5,6], 3)
    print(nums1)

    nums2 = [1]
    s.merge(nums1, 1, [], 0)
    print(nums2)

    nums3 = [2,0]
    s.merge(nums3, 1, [1], 1)
    print(nums3)