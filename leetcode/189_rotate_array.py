class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        ''' O(n) time, O(n) space '''
        n = len(nums)
        k = k % n
        rotated = nums[n-k:] + nums[:n-k]
        for i in range(n):
            nums[i] = rotated[i]


    def rotateReverse(self, nums: list[int], k: int) -> None:
        ''' O(1) time, O(1) space '''
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:]) 


if __name__ == "__main__":
    s = Solution()

    nums1 = [1,2,3,4,5,6,7]
    s.rotate(nums1, 3)
    print(nums1)

    nums1 = [-1,-100,3,99]
    s.rotate(nums1, 2)
    print(nums1)

    nums1 = [1,2]
    s.rotate(nums1, 0)
    print(nums1)

    nums1 = [1,2]
    s.rotate(nums1, 5)
    print(nums1)