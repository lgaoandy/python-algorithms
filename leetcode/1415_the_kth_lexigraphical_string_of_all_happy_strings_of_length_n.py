class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        res = ""
        
        def find_string(i, arr):
            nonlocal k, res
            
            if i == n:
                k -= 1
                if k <= 0:
                    res = "".join(arr)
                return
            
            for char in chars:
                if k <= 0:
                    continue
                if i != 0 and arr[i-1] == char:
                    continue
                else:
                    arr[i] = char
                    find_string(i+1, arr)
                    arr[i] = 0
                    
        find_string(0, [0] * n)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.getHappyString(1,3))
    print(s.getHappyString(1,4))
    print(s.getHappyString(3,9))