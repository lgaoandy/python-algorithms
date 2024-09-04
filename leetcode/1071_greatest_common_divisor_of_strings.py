import math

class Solution():
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        # find the shorter string
        divisor = min(str1, str2, key=len)
        longer_str = max(str1, str2, key=len)

        # if same length but different values, this is impossible and returns none
        if len(str1) == len(str2) and str1 != str2:
            return ""

        # test divisor until found
        while True:
            if len(divisor) == 0:
                return ""
            if len(longer_str) % len(divisor) != 0:
                divisor = divisor[:-1]
                continue
            
            for i in range(int(len(longer_str) / len(divisor))):
                if longer_str[i * len(divisor):(i + 1) * len(divisor)] != divisor:
                    divisor = divisor[:-1]
                    continue
            return divisor
    
    # Weaknesses from PHIND
    # 1) inefficient loop - time complexity of O(n^2)
    # 2) repetition in loop body
    # 3) solution doesn't take advantage of string properties
    def gcd_of_strings_optimized(self, str1: str, str2: str) -> str:
        # define l, s as lengths
        # define l, str1 being larger than s, str2 if applicable
        l, s = len(str1), len(str2)
        if l < s:
            l, s = s, l
            str1, str2 = str2, str1

        # find gcd & divisor
        gcd = math.gcd(l, s)
        divisor = str2[:gcd]
        print("-")
        print(divisor)

        # check if strings are divisible by divisor
        for i in range(0, s, gcd):
            print(i, str1[i:i+gcd], str2[i:i+gcd])
            if str1[i:i+gcd] != divisor or str2[i:i+gcd] != divisor:
                return ""
        
        for i in range(s, l, gcd):
            if str1[i:i+gcd] != divisor:
                return ""
        return divisor

    
if __name__ == "__main__":
    solution = Solution()
    # print(solution.gcd_of_strings("ABCABC", "ABC"))
    # print(solution.gcd_of_strings("ABABAB", "ABAB"))
    # print(solution.gcd_of_strings("LEET", "CODE"))
    print(solution.gcd_of_strings_optimized("ABCABC", "ABC"))
    print(solution.gcd_of_strings_optimized("ABABAB", "ABAB"))
    print(solution.gcd_of_strings_optimized("LEET", "CODE"))
    print(solution.gcd_of_strings_optimized("AAAAAAAAA", "AAACCC"))

# What I learned
# - you can switch variable values using comma separation 
# - math.gcd()
# - range() accept start, end and step params
