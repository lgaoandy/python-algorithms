class Solution:
    '''
        pseudo-code:
        - make 2 pointers and max_area
        - move pointers closer depending on which side is taller
    '''
    def container_with_most_water(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = abs(r - l) * min(height[l], height[r])

        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1  
            area = abs(r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
        return max_area

if __name__ == "__main__":
    test = Solution()
    print(test.container_with_most_water([1,8,6,2,5,4,8,3,7]))
    print(test.container_with_most_water([1,1]))