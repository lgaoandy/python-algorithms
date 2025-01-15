class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_num1 = bin(num1)
        bit_num2 = bin(num2)

        # Count the number of set bits in num1 and num2
        bit_count_num1 = bit_num1.count("1")
        bit_count_num2 = bit_num2.count("1")

        # If num1 has more set bits than num2, remove some set bits from num1
        while bit_count_num1 > bit_count_num2:
            num1 &= num1 - 1
            bit_count_num1 -= 1

        # If num1 has fewer set bits than num2, add set bits to num1
        while bit_count_num1 < bit_count_num2:
            num1 |= (num1 + 1)
            bit_count_num1 += 1

        return num1


if __name__ == "__main__":
    s = Solution()
    print(s.minimizeXor(3, 6))
    print(s.minimizeXor(1, 12))