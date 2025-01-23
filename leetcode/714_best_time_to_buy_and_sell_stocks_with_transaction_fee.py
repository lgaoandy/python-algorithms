class Solution:
    '''
        Intuition
        - We only need to find the maximum profit, meaning we do not need to know how to get there
        - Transactional fee sets the min difference you can profit from a buy and sell

        Dynamic Programming Approach
        - 
    '''
    def max_profit_with_grid(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        profits = [[0] * n] * n
        max_profits = [0] * n
        
        for i in range(0, n):
            for j in range(i+1, n):
                current_sell = prices[j] - prices[i] - fee

                # append max of the previous value
                if i >= 2 and j >= 2:
                    current_sell += max_profits[i-1]

                profits[i][j] = max(0, current_sell, profits[i][j-1])
                max_profits[j] = max(max_profits[j], profits[i][j])
        return max_profits[-1]
    

    def max_profit(self, prices: list[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell


if __name__ == "__main__":
    s = Solution()
    # print(s.max_profit([1,3,2,8,4,9], 2))
    # print(s.max_profit([1,3,7,5,10,3], 3))
    # print(s.max_profit([1,3,2,8,4,9], 2))
    # print(s.max_profit([1,4,6,2,8,3,10,14], 3))
    print(s.max_profit([1,2,1,5,3,5,5,4,1,5], 0))