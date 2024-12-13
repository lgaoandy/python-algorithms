import string

class Solution:
    '''
        pseudo-code
        - using a stack, loop through str
            - if a num or letter is found, check if previous item is of the same type, if it is combine them, then append
            - if a "]" bracket is found, loop through stack until a number is found, then write to results
    '''
    def decode_string(self, s: str) -> str:
        stack = []
        split = False
        for char in s:
            if char.isnumeric(): 
                if split == False and len(stack) > 0 and stack[-1].isnumeric():
                    stack[-1] = stack[-1] + char
                else:
                    stack.append(char)
                    split = False
            elif char in string.ascii_lowercase:
                stack.append(char)
            elif char == "]":
                substring = []
                while stack[-1].isnumeric() == False:
                    substring.insert(0, stack.pop())
                stack.append(int(stack.pop()) * "".join(substring))
            else:
                split = True
        return "".join(stack)

if __name__ == "__main__":
    test = Solution()
    print(test.decode_string("3[a]2[bc]"))
    print(test.decode_string("3[a2[c]]"))
    print(test.decode_string("2[abc]3[cd]ef"))
    print(test.decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))