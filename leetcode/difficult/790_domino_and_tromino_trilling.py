class Solution:
    '''
        Intuition
        - In a given sequence n, we can define F(n) as the number of orientations possible to fill n spaces in a 2 x n grid

        - Let's consider the cases in which to calculate F(n)
            - Scenario a - one possibility is a domino standing in a column occupying a single 1 x n, in this case, we can conclude F(n)_a = F(n-1)
            - Scenario b - Another possibility is having 2 dominos placed horizontally, occupying 2 x n, in this case, F(n)_b = F(n-2)
            - Scenario c - As for the last two possibilities, we consider the different orientations a tromino can be placed, that is either with the top missing or bottom missing
                - In these iterations, we can conclude that we also need T(n), defined the same as F(n) but with the top rightmost tile missing, and similar bottom rightmost missing for B(n)
                - Thus F(n)_c = T(n-1) + B(n-1)
            - Combining all possible scenarios: 
                F(n) = F(n-1) + F(n-2) + T(n-1) + B(n-1)
            - Start values:
                F(0) = 1 (domino standing vertical)
                F(1) = 2 (2 domino standing vertical OR 2 domino standing horizontal)

        - We also have to consider the possibilities for T(n) and B(n):
            - When we have a top missing, we can place a bottom oriented trodomino to turn the rest of the tiles as full, thus T(n)_1 = F(n-2)
            - There's also the chance that a domino is place in midst of the bottom tile creating a bottom missing tile as a following, thus T(n)_2 = B(n-1)
            - Thus, we end for these 2 equations:
                T(n) = F(n-2) + B(n-1)
                B(n) = F(n-2) + T(n-1)
            - Now, let's consider the start values of these:
                T(0) = B(0) = 0 (not possible to place a tridomino on 1 x 2)
                T(1) = B(1) = 1 (place either with long head top or bottom)
                - Consider this values are the same, and the 2 relationship equations mirror, we can collapse them as one value T (for tridomino):
                    F(n) = F(n-1) + F(n-2) + 2T(n-1)
                    T(n) = F(n-2) + T(n-1)

        Dynamic Programming Approach
        - Using the equations above, define default solutions for when n = 1 and n = 2
        - Iterate from 3 to n, calculating F(n) along the way
    '''
    def num_trilling(self, n: int) -> int:
        f = [0,1,2] + [0] * (n-2)
        t = [0,0,1] + [0] * (n-2)

        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2] + 2 * t[i-1]
            t[i] = f[i-2] + t[i-1]
        return f[n] % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    print(s.num_trilling(1))
    print(s.num_trilling(2))
    print(s.num_trilling(3))
    print(s.num_trilling(4))
    print(s.num_trilling(5))
    print(s.num_trilling(6))
    print(s.num_trilling(30))