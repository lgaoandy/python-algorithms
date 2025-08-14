class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # setup largest as the largest digit with a successful triplet
        largest = -1

        # setup p as the previous digit
        p0 = int(num[0])
        p1 = int(num[1])

        # iterate digits in num
        for i in range(2, len(num)):
            c = int(num[i])
            if p0 == p1 == c:
                if c > largest:
                    largest = c
            p0, p1 = p1, c
        
        return str(largest) * 3 if largest >= 0 else ""
            

if __name__ == "__main__":
    s = Solution()
    print(s.largestGoodInteger("6777133339"))
    print(s.largestGoodInteger("2300019"))
    print(s.largestGoodInteger("42352338"))