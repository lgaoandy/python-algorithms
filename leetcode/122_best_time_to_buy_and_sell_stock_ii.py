class Solution:
    '''
        Intuition
        - Dry run:  1, 3, 5 - concern is if there is higher number than the current, how do you know when to sell?
        - Going from 1 to 3, we see a profit of 2, we sell it then buy it again
        - Going from 3 to 5, we see another profit margin of 2, we sell then buy it again
        - Overall, it makes no difference when we buy or sell since we can buy and sell on the same day
        - Therefore, we must always update the prices after a sell to the current price
        - Since, we always update buy price, there is no reason store it as a integer, we can simply compare to the previous value
    '''
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([1,2,3,4,5]))