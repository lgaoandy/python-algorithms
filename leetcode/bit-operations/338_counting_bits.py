class Solution:
    '''
        Dry run:
        0   0000            0000        dp[0] = 0
        1   0001    pow 0   0001 + []   dp[1] = dp[0] + 1   i-1
        2   0010    pow 1   001 + [0]   dp[2] = dp[0] + 1   i-2
        3   0011            001 + [1]   dp[3] = dp[1] + 1   i-2
        4   0100    pow 2   01 + [00]   dp[4] = dp[0] + 1   i-4
        5   0101            01 + [01]   dp[5] = dp[1] + 1   i-4
        6   0110            01 + [10]   dp[6] = dp[2] + 1   i-4
        7   0111            01 + [11]   dp[7] = dp[3] + 1   i-4
        8   1000    pow 3   1 + [000]   dp[8] = dp[0] + 1   i-8
        9   1001            1 + [001]   dp[9] = dp[1] + 1   i-8
        10  1010            1 + [010]   dp[10] = dp[2] + 1  i-8
        11  1011            1 + [011]   dp[11] = dp[3] + 1  i-8
        12  1100            1 + [100]   dp[12] = dp[4] + 1  i-8
        13  1101            1 + [101]   dp[13] = dp[5] + 1  i-8
        14  1110            1 + [110]   dp[14] = dp[6] + 1  i-8
        15  1111            1 + [111]   dp[15] = dp[7] + 1  i-8
        16 10000    pow  4  1 + [0000]  dp[16] = dp[0] + 1  i-16
    '''
    def count_bits(self, n: int) -> list[int]:
        ones = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ones[i] = ones[i - offset] + 1
        return ones


if __name__ == "__main__":
    s = Solution()

    print(s.count_bits(3))
    print(s.count_bits(64))