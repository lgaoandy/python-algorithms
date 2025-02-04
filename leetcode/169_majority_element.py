class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        occurrences = {i:0 for i in set(nums)}
        for num in nums:
            occurrences[num] += 1
        ans = ""
        max_seen = 0
        for i in occurrences.keys():
            if occurrences[i] > max_seen:
                ans = i
                max_seen = occurrences[i]
        return ans
    

    def majorityElementHashMap(self, nums: list[int]) -> int:
        '''Hashmap approach - O(n) time, O(n) space'''
        n = len(nums) / 2
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > n:
                return num
    

    def majorityElementMooreVoting(self, nums: list[int]) -> int:
        '''Moore Voting - O(n) time, O(1) space'''
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    s = Solution()

    print(s.majorityElement([3,2,3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))