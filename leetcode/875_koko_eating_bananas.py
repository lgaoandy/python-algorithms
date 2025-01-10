from math import ceil

class Solution:
    '''
        Constriants:
        - piles.length <= h <= e9 - it is always possible for koko to eat all banana piles
        - 1 <= piles[i] <= e9 - banana piles cannot be empty, meaning the minimum amount of hours koko needs to spend in each pile is one

        Comments/questions for interviewer
        - length of piles and h should evaluated first, as the results are heavily dependent on their relationship
        - simplest case is when length of pile == h, in which case, k will be the max(piles[i]) - which demands O(n) time complexity
        - piles should be sorted
        - we set a boundaries for possible min and max values of k and find k by binary search

        Pseudo-code
        - evaluate the amount of piles and h
        - if h == piles.length, find max of piles[i]
        - if h > piles.length, sort piles, then take a greedy approach

        Analysis
        - time complexity: O(nlogn) + O(nlog(max(piles[i]))) = O(nlog(n + max(piles[i])))

    '''
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)

        # handle simplest cases
        if n == h:
            k = 0
            for i in piles:
                k = max(k, i)
            return k
        elif n == 1:
            return ceil(piles[0] / h)

        piles.sort()

        # set up a binary search for value of k
        min_k = ceil(piles[0] / h)
        max_k = piles[-1]

        while min_k != max_k:
            guess_k = (min_k + max_k) // 2
            hours = 0

            for i in piles:
                hours += ceil(i / guess_k)
                if hours > h:
                    min_k = guess_k + 1
                    break
            
            if hours <= h:
                max_k = guess_k
        return min_k


if __name__ == "__main__":
    s = Solution()
    print("ans:", s.minEatingSpeed([3,6,7,11],8)) # 4
    print("ans:", s.minEatingSpeed([30,11,23,4,20],5)) # 30
    print("ans:", s.minEatingSpeed([30,11,23,4,20],6)) # 23
    print("ans:", s.minEatingSpeed([312884470],312884469)) # 2