class Solution:
    '''
        Counting Approach [DID NOT WORK]
        - Traverse through costs, evaluate the cheapest in next two steps, then add cost to total cost
    '''
    def min_cost_climbing_stairs_counting(self, cost: list[int]) -> int:
        # Start by defining an index value
        i = -1 # Start at negative one because we don't start on the staircase
        n = len(cost)
        total_cost = 0
        
        # While staircase is not fully traversed, we traverse
        while i < n - 2:
            i += 2 if cost[i+1] > cost[i+2] else 1
            total_cost += cost[i]
        return total_cost
        
        
    '''
        Dyanmic Programming Approach
        - Define a min_cost as an array - each index represents the min_cost to that specific index from -1
        - Traverse through rest of staircase, evaluating the previous two values of min_cost to determine current step
        - Time complexity: O(n)
        - Space complexity: O(n)
    '''
    def min_cost_climbing_stairs(self, cost: list[int]) -> int: 
        # Take the first two elements of the staircase, the cost to travel to them are itself because of the value
        min_cost = cost[:2]
        n = len(cost)
        
        for i in range(2, n):
            prev_min = min(min_cost[i-1], min_cost[i-2])
            min_cost.append(prev_min + cost[i])
        return min(min_cost[n-1], min_cost[n-2])

if __name__ == "__main__":
    s = Solution()
    print(s.min_cost_climbing_stairs([10,15,20]))
    print(s.min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))