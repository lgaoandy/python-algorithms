'''
    Constriants:
    - 1 <= s.length <= 10^5
    - s consists only lowercase english letters and * # and %
    - 0 <= k <= 10^15
'''
class Solution:
    # Time - O(len(s))
    # Space - O(s^s)
    def processStrBruteForce(self, s: str, k: int) -> str:
        results = []
        
        for ch in s:
            if ch == '*':
                if results:
                    results.pop()
            elif ch == '#':
                    results.extend(results.copy())
            elif ch == '%':
                results.reverse()
            else:
                results.append(ch)
        
        if len(results) <= k:
            return '.'
        return results[k]


    '''
        Thoughts / Pseudo-code
        1) The brute force method is not a feasible solution due to space complexity O(s^s).
            - Thus, it is also not feasible to build the results string by follow the str operations 
            
        2) We only care about the value in the k-th position - a single char in the entire string
            - Thus, instead of building the results string, we can track the length of the results string per operation, until the k-th element is printed
            - However, we cannot just return the value of the k-th position at first instance it is populated, due to the 'delete' and 'reverse' operations
            - This means that the end solution must iterate through the entire s string AT LEAST ONCE
            
        3) Given  we do iterate through the entire s operation, then the final length of the results string would also be known
        
        4) If we know the end length of the results string, we can iterate the s string in reverse order
            - this time as soon as the value of kth element is reached, we CAN return this value
        
        5) However, we need to consider the 3 special operations .
            - In reverse order, if we find a '*' [delete] operation, we add to the length value
            - If we find a '%' or [reverse] operation, we update the value of k: abs(n - k) - 1
            - If we find a '#' or [duplicate] operation, 
                    we half the length: n = n / 2
                    and if k is within that length: k = k - n 
            
        Analysis
        - time complexity: O(n)
        - space complexity: O(1)
    '''
    def processStr(self, s: str, k: int) -> str:
        # calculate end-length
        n = 0
        for c in s:
            if c == '*' and n:
                n -= 1
            elif c == '#':
                n *= 2
            elif c == '%':
                pass
            else:
                n += 1
                
        # check for out of bound
        if n <= k:
            return '.'
        
        # iterate in reverse order until a lowercase letter is found
        for c in reversed(s):
            if c == '*':
                n += 1
            elif c == '#':
                if k + 1 > (n + 1) // 2:
                    k -= n // 2
                n = (n + 1) // 2
            elif c == '%':
                k = abs(n - k) - 1
            else:
                if k + 1 == n:
                    return c
                n -= 1


if __name__ == "__main__":
    s = Solution()
    
    print(s.processStr("a#b%*", 1))
    print(s.processStr("cd%#*#", 3))
    print(s.processStr("z*#", 0))