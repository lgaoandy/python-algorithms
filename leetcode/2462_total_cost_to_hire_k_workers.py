import heapq

class Solution:
    '''
        constriants:
        - 1 <= costs.length <= e5
        - 1 <= costs[i] <= e5
        1 <= k, candidates <= costs.length

        comments/questions for interviewer
        - N/A

        pseudo-code
        - create a list of pairs - representing the available candidate pool of the current hiring round, storing the cost to hire and whether they are from left or right
        - sort list of pairs by the cost to hire
        - leave any remainings from costs if applicable
        - after sorting, we find the lowest values, if there are two values, prioritize "left"
        - then take another candidate from the side it is hired from if applicable
        - repeat pattern k times, return total cost

        analysis
        - time complexity: O(klog(cost + k))
    '''
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        total_cost = 0
        pairs = []

        # get candidates of current round from left
        for _ in range(min(len(costs), candidates)):
            cost = costs.pop(0)
            heapq.heappush(pairs, (cost, "L"))

        # get candidates of current round from right
        for _ in range(min(len(costs), candidates)):
            cost = costs.pop()
            heapq.heappush(pairs, (cost, "R"))

        # # hire k times
        for _ in range(k):
            # hire lowest cost
            cost, placement = heapq.heappop(pairs)
            total_cost += cost

            # check if there is a hire with the same score on the left
            if placement == "R":
                temp = []
                while len(pairs):
                    x, y = heapq.heappop(pairs)
                    if x == cost and y == "L":
                        cost, placement = x, y # swap with current
                        break

                    temp.append((x, y))
                    if x > cost:
                        break
                
                # push back all temp
                for pair in temp:
                    heapq.heappush(pairs, pair)
            
            # replenish worker from remaining
            if len(costs) > 0:
                if placement == "L":
                    heapq.heappush(pairs, (costs.pop(0), "L"))
                else:
                    heapq.heappush(pairs, (costs.pop(), "R"))
        return total_cost


    '''
        Optimization:
        - uses two heaps
        - uses pointers to track remaining hires if available, not mutating costs, saves time/space
    '''
    def totalCost2(self, costs: list[int], k: int, candidates: int) -> int:
        q = costs[:candidates]
        qq = costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(q)
        heapq.heapify(qq)
        ans = 0 
        i, ii = candidates, len(costs)-candidates-1
        for _ in range(k): 
            if not qq or q and q[0] <= qq[0]: 
                ans += heapq.heappop(q)
                if i <= ii: 
                    heapq.heappush(q, costs[i])
                    i += 1
            else: 
                ans += heapq.heappop(qq)
                if i <= ii: 
                    heapq.heappush(qq, costs[ii])
                    ii -= 1
        return ans 


if __name__ == "__main__":
    s = Solution()
    print(s.totalCost2([17,12,10,2,7,2,11,20,8],3,4)) # 11
    print(s.totalCost2([1,2,4,1],3,3)) # 4