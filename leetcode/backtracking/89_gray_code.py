class Solution:
    '''
        Constriants:
        - 1 <= n <= 16, the max bit amount is 16

        Brute Force Backtrack Approach
        - 
    '''
    def grey_code_brute_force(self, n: int) -> list[int]:
        m = pow(2, n)

        # convert all numbers to bits
        bits = { i:0 for i in range(m) }
        for i in range(m):
            bits[i] = bin(i)[2:].zfill(n)

        # Check if two bits are one bit part
        def one_bit_diff(bit1, bit2):
            count = 0
            for i in range(n - 1, -1, -1):
                if bit1[i] != bit2[i]:
                    if count > 0:
                        return False
                    count += 1
            return count == 1
        
        res = []
        def backtrack(i, current, remaining):
            nonlocal res

            if len(res) > 0:
                return
            
            if len(current) == m:
                if one_bit_diff(bits[current[0]], bits[current[m - 1]]):
                    res = current.copy()

            for num in range(m):
                if num in remaining and one_bit_diff(bits[current[i]], bits[num]):
                    remaining.remove(num)
                    current.append(num)
                    backtrack(i+1, current, remaining)
                    current.pop()
                    remaining.add(num)

        backtrack(0, [0], set(range(1, m)))
        return res
    

    def grey_code_bitwise(self, n: int) -> list[int]:
        if n == 1:
            return [0, 1]
        
        nums = ["0", "1"]
        count = 1
        m = len(nums)

        while count < n:
            for i in range(m - 1, -1, -1):
                nums.append("1" + nums[i])
            for i in range(m):
                nums[i] = "0" + nums[i]
            count += 1
            m = len(nums)

        res = []
        for bits in nums:
            mult = 1
            value = 0
            for i in range(n - 1, -1, -1):
                if bits[i] == "1":
                    value += mult
                mult *= 2
            res.append(value)
        return res
                

if __name__ == "__main__":
    s = Solution()

    print(s.grey_code_bitwise(1))
    print(s.grey_code_bitwise(2))
    print(s.grey_code_bitwise(3))
    print(s.grey_code_bitwise(4))
    print(s.grey_code_bitwise(5))
    print(s.grey_code_bitwise(6))

    # print(s.grey_code_brute_force(1))
    # print(s.grey_code_brute_force(2))
    # print(s.grey_code_brute_force(3))
    # print(s.grey_code_brute_force(4))

