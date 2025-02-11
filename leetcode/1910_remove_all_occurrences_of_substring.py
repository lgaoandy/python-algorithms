class Solution:
    '''
        Intuition
        - Substring - defined as a continguous sequence of characters
        - Minimum required time complexity for this problem is O(n) - we must see every letter at least once
        - Stack can used to track if the most recently sequence is apart of the substring to be removed
        - We can keep track of the progress using a number i representing the value of the current stack that is matching the index of the substring if applicable

        Stack Approach
        - Set up a stack and an index counter
        - Iterate through the string, check if the current letter matches the next char in the substring given the index counter
            - e.g.  in a "abcdefg", "abc"
            - index-counter initialized at -1, the next index it looks for is 0, which is "a"
        - If at a completed substring has been matched, we remove the length of substring chars off the stack
    '''
    def removeOccurrences_1stAttempt(self, s: str, part: str) -> str:
        stack = []
        index = 0
        n = len(part) - 1
        
        for i in s:
            if i == part[index]:
                if index == n:
                    stack = stack[:-n]
                    index = 0
                    continue
                index += 1
            elif i == part[0]:
                index = 1
            else:
                index = 0
            stack.append(i)
        return stack
    
    
    def removeOccurrences(self, s: str, part: str) -> str: 
        ''' Make it simplier, append letters, if the letter is the last letter of the substring, check backwards '''
        stack = []
        n = len(part)
        
        def check_substring():
            i = len(stack) - 1
            j = len(part) - 1
            while stack[i] == part[j] and i >= 0 and j >= 0:
                if j == 0:
                    return True
                i -= 1
                j -= 1
            return False
        
        for i in s:
            stack.append(i)
            if i == part[n-1]:
                if check_substring():
                    stack = stack[:-n]
                    continue
        return "".join(stack)


    def removeOccurrencesOptimal(self, s: str, part: str) -> str: 
        while part in s:
            s = s.replace(part, "", 1)
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.removeOccurrences("daabcbaabcbc", "abc"))
    print(s.removeOccurrences("axxxxyyyyb", "xy"))
    print(s.removeOccurrences("gjzgbpggjzgbpgsvpwdk", "gjzgbpg"))