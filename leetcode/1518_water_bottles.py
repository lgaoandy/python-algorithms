class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        bottles = numBottles
        while bottles >= numExchange:
            ans += bottles // numExchange
            bottles = bottles // numExchange + bottles % numExchange
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numWaterBottles(9, 3))
    print(s.numWaterBottles(15, 4))
    print(s.numWaterBottles(12, 4))