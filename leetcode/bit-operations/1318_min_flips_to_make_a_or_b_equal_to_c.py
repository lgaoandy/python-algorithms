from math import log2, floor

class Solution:
    '''
        Dry runs:
            ex1)
                a = 2   0010
                b = 6   0110
                ------------
                aXORb   0110
                c = 5   0101
            ex2)
                a = 4   0100
                b = 2   0010
                ------------
                aXORb   0110
                c = 7   0111

        Intuition:
        - If 0, both bits must be zero
        - If 1, only one of the bits need to be one

        Approach:
        - Write a function getting all 1 bit placements of an integer
        - Get 1 bit placements for all three integers given
        - Check 1s from c (end goal), if there is no 1s in both a and b, add 1 to count (becase at least 1 bit must be present here)
        - Remove this placement from any set that has this
        - To check for 0s, simply add the length of both a and b remaining (they must be 0s)

        Time complexity: O(n), Space complexity: O(n)
    '''
    def min_flips(self, a: int, b: int, c: int) -> int:
        def get_one_bits(n):
            res = set()
            while n > 0:
                m = floor(log2(n))
                res.add(m)
                n = n - pow(2, m)
            return res

        a_ones = get_one_bits(a)
        b_ones = get_one_bits(b)
        c_ones = get_one_bits(c)

        count = 0
        # check 1s
        for i in c_ones.copy():
            if i not in a_ones and i not in b_ones: # if neither has a one
                count += 1
            else:
                if i in a_ones:
                    a_ones.remove(i)
                if i in b_ones:
                    b_ones.remove(i)
                c_ones.remove(i)
        
        # check 0s
        return count + len(a_ones) + len(b_ones)


if __name__ == "__main__":
    s = Solution()
    print(s.min_flips(2,6,5))
    print(s.min_flips(4,2,7))
    print(s.min_flips(1,2,3))
