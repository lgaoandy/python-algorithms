class Solution:
    '''
        Brute Force Approach
        - Initialize ans as an array of zeros in the size of temperature
        - Iterate from end of list, find the closest day warmer than current day using a pointer
        - Time complexity: O(n^2)
    '''
    def dailyTemperaturesBruteForce(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        it_gets_in_warmer_in = [0] * n
        
        for i in range(n-2, -1, -1):
            j = 0
            while True:
                j += 1
                if temperatures[i+j] > temperatures[i]:
                    break
                if i + j == n - 1:
                    j = 0
                    break
            
            it_gets_in_warmer_in[i] = j
        return it_gets_in_warmer_in
    

    def dailyTemperaturesMonotonicStack(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(s.dailyTemperatures([30,40,50,60]))
    print(s.dailyTemperatures([30,60,90]))