class Solution():
    def kids_with_candies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # get greatest candy
        greatest = max(candies)

        result = []
        for i in candies:
            result.append(i + extraCandies >= greatest)
        return result

    def kids_with_candies_idiomatic(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        return [candy + extraCandies >= greatest for candy in candies]


if __name__ == "__main__":
    solution = Solution()
    print(solution.kids_with_candies([2,3,5,1,3], 3))
    print(solution.kids_with_candies([4,2,1,1,2], 1))
    print(solution.kids_with_candies_idiomatic([2,3,5,1,3], 3))
    print(solution.kids_with_candies_idiomatic([4,2,1,1,2], 1))

# What I learned
# - you can write simple for loops into one line