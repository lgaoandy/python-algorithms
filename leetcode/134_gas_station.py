class Solution:
    '''
        Approach
        - Combine gas + cost by index - net_gas
        - Iterate through net_gas, recording all 
    '''
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        ''' O(n) time, O(1) space '''
        n = len(gas)
        net_sum = 0
        index = -1
        cur = 0
            
        for i in range(n):
            net_gas = gas[i] - cost[i]

            # replace to current index if previous index failed
            if cur <= 0 and net_gas >= 0: 
                index = i
                cur = 0
            cur += net_gas
            net_sum += net_gas
        
        if net_sum < 0:
            return -1
        return index


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
    print(s.canCompleteCircuit([2,3,4],[3,4,3]))
    print(s.canCompleteCircuit([3,1,1],[1,2,2]))
    print(s.canCompleteCircuit([2],[2]))