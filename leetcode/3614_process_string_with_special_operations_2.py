'''
    Constriants:
    - 1 <= s.length <= 10^5
    - s consists only lowercase english letters and * # and %
    - 0 <= k <= 10^15

    Thoughts
    - We only need to track two characters - the k-th character and the k-th character if the string is reversed. Anything else doesn't matter
    - Setup a counter representing the length

    Pseudo-code
    - iterate linked list from start to end to get length n
    - using logic above to find the m, the middle node
    - iterate second pass, on the m-1 node, replace the next node as the next node after the middle node, consequently removing the node and return

    Analysis
    - time complexity: O(n)
    - space complexity: O(1)
'''
class Solution:
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


if __name__ == "__main__":
    s = Solution()
    
    print(s.processStrBruteForce("a#b%*", 1))
    print(s.processStrBruteForce("cd%#*#", 3))
    print(s.processStrBruteForce("z*#", 0))