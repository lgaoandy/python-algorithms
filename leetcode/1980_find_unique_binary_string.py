class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        res = ""
        nums = set(nums)
        
        def find(i, arr):
            nonlocal res
            binary = "".join(arr)
            
            if binary not in nums:
                res = binary
                return
            if i > n-1:
                return
            
            for j in ["0", "1"]:
                if res != "":
                    continue
                arr[i] = j
                find(i+1, arr)
        
        find(0, ["0"] * n)        
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.findDifferentBinaryString(["01","10"]))
    print(s.findDifferentBinaryString(["00","01"]))
    print(s.findDifferentBinaryString(["111","011","001"]))
    print(s.findDifferentBinaryString(["0"]))