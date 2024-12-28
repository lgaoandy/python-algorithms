class Solution:
    '''
        constriants:
        - number of values: [2, 5e4]
        - values: [1, 1000]

        pseudo-code
        - dynamic programming
        - keep track of the score of the max pair by each index

        analysis
        - 
    '''
    def sight_seeing_pair(self, values: list[int]) -> int:
        res = 0
        cur_max = values[0] # at index zero, the max value is itself
        for i in range(1, len(values)):
            cur_max -= 1 # for each incremental distance, we substract one (as its equivalent value to the current num)
            res = max(res, values[i] + cur_max)
            cur_max = max(cur_max, values[i])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.sight_seeing_pair([8,1,5,2,6]))
    print(s.sight_seeing_pair([1,2]))
    print(s.sight_seeing_pair([1,3,5]))
    print(s.sight_seeing_pair([1,2,2]))
    print(s.sight_seeing_pair([2,7,7,2,1,7,10,4,3,3]))
    