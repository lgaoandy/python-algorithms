class Solution:
    '''
        Intuition
        - Every kid must have one candy, this is baseline
        - We can use slopes to determine how much candy to add after that
        - Iterating from one end to another, we can determine the current slope
            - For example, 1, 2, 3, 4, an increasing slope, adds 1 on the next value as long as the slope continues

        Approach
        - Iterate from left to right, then right to left
    '''
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        slope = [0] * n

        # check increasing slopes
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                slope[i] = slope[i-1] + 1
        
        # check decreasing slopes but take the max of the slope values
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                slope[i] = max(slope[i], slope[i+1] + 1)
        
        # answer is the sum of slopes plus n (at least 1 candy per kid)
        return sum(slope) + n


if __name__ == "__main__":
    s = Solution()
    print(s.candy([1,0,2]))
    print(s.candy([1,2,2]))