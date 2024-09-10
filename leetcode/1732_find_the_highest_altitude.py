class Solution():
    '''
        pseudo-code
        - loop through list, adding each change in altitude, storing max
    '''
    def largest_altitude(self, gain: list[int]) -> int:
        attitude = 0
        highest_attitude = 0
        for change in gain: 
            attitude += change
            highest_attitude = max(highest_attitude, attitude)
        return highest_attitude
    
    # make an array of attitude at any given point then get max
    def largest_altitude_prefix_sum(self, gain: list[int]) -> int:
        attitudes = [0]
        for i in range(len(gain)):
            attitudes.append(attitudes[i] + gain[i])
        return max(attitudes)

if __name__ == "__main__":
    test = Solution()
    print(test.largest_altitude([-5,1,5,0,-7]))
    print(test.largest_altitude([-4,-3,-2,-1,4,3,2]))
    print(test.largest_altitude_prefix_sum([-5,1,5,0,-7]))
    print(test.largest_altitude_prefix_sum([-4,-3,-2,-1,4,3,2]))