class Solution():
    '''
        pseudo-code
        - loop through str
        - when a star is found, save current pointer as star start
            - when the next char is found, get the length of the star area using the star start
            - convert all char area and star area into _
    '''
    def remove_stars(self, s: str) -> str:
        star_start = -1
        i = 0
        while i < len(s):
            if s[i] == "*" and star_start == -1:
                star_start = i
            if (i+1 >= len(s) or s[i+1] != "*") and star_start != -1:
                star_length = i - star_start + 1
                s = s[0:star_start - star_length] + s[i+1:]
                star_start = -1
                i -= star_length * 2 - 1
            i += 1
        return s
    
    '''
        solution from Leetcode:
        - using stack simplifies this problem a lot
    '''
    def remove_stars_stack(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

if __name__ == "__main__":
    test = Solution()
    # print(test.remove_stars("leet**cod*e"))
    # print(test.remove_stars("erase*****"))
    # print(test.remove_stars("asfdsf"))
    print(test.remove_stars_stack("leet**cod*e"))
    print(test.remove_stars_stack("erase*****"))
    print(test.remove_stars_stack("asfdsf"))

    '''
        What to recognize stack problems:
        - last-in-first-out behaviours
        - reversal of orders
        - backtracking scenarios
        - undo/redo functionalities
    '''