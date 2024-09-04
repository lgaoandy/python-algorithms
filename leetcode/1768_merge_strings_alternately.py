class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        # find the longest length between 2 words
        longest = max(len(word1), len(word2))

        # setup result
        result = ""

        # loop through range, merging alternatively
        for i in range(longest):
            if len(word1) >= i + 1:
                result += word1[i]
            if len(word2) >= i + 1:
                result += word2[i]
        return result
    
    # Weaknesses from PHIND
    # 1) redundant checks - checking len(word1) and len(word2) in every iteration is unnecessary since these lengths don't change
    # 2) string concatenation - list + join() is faster than string concatenation
    def merge_alternately_optimized(self, word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1), len(word2))

        # use min length guarantees that both strs merge, eliminating the need to check
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        # using the string range operator to concat the rest
        result.extend(word1[min_len:])
        result.extend(word2[min_len:])

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge_alternately("ab", "cdefg"))
    print(solution.merge_alternately_optimized("ab", "cdefg"))

# What I learned
# - when two pointers are involved in a loop, use the min loop to simplify the problem
# - .join() method is more resource efficient than string concatenation
# - difference between .extend() and .append() methods are that .extend() adds multiple elements from iterables while .append adds as single item