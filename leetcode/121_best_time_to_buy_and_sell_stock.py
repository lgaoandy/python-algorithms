class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        profit = 0

        for price in prices:
            if price > min_price:
                profit = max(profit, price - min_price)
            else:
                min_price = price
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))