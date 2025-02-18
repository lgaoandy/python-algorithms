class Solution:
    '''
        Intuition
        - Greedy backtracking - prioritize smallest lexicographically nums first
    '''
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [0] * (n+1)
        num_range = range(1, n+2)
        availabe = set([i for i in num_range])
        
        def construct(i):
            if i >= n + 1: # base case
                return True
            for num in num_range:
                if num not in availabe:
                    continue
                if i != 0 and pattern[i-1] == "I" and res[i-1] > num:
                    continue
                if i != 0 and pattern[i-1] == "D" and res[i-1] < num:
                    continue
                
                res[i] = num
                availabe.remove(num)
                if construct(i+1):
                    return True
                availabe.add(num)
        construct(0)
        return "".join(map(str, res))


if __name__ == "__main__":
    s = Solution()
    print(s.smallestNumber("IIIDIDDD"))
    print(s.smallestNumber("DDD"))