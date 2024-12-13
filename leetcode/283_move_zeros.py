class Solution:
    '''
        Pseudo code
        1) setup a zero pointer and num pointer
        2) loop nums in reverse, when a zero 
    '''
    def move_zeroes(self, nums: list[int]) -> None:
        zero_pointer = 0
        num_pointer = 0

        while num_pointer < len(nums) and zero_pointer < len(nums):
            if nums[zero_pointer] == 0 and nums[num_pointer] != 0 and zero_pointer < num_pointer:
                nums[zero_pointer], nums[num_pointer] = nums[num_pointer], nums[zero_pointer]
                zero_pointer += 1
                num_pointer += 1
            else:
                if nums[zero_pointer] != 0:
                    zero_pointer += 1
                if nums[num_pointer] == 0 or zero_pointer > num_pointer:
                    num_pointer += 1
        return nums

if __name__ == "__main__":
    solution = Solution()

    nums1 = [0,1,0,3,12]
    solution.move_zeroes(nums1)
    print(nums1)

    nums2 = [0]
    solution.move_zeroes(nums2)
    print(nums2)

    nums3 = [1, 0]
    solution.move_zeroes(nums3)
    print(nums3)

    # What I learned:
    # - when using two pointers going from the same side, make it simple by setting increment to 1 per iteration