class Solution:
    '''
        Pseudo code
        1) trim string
        2) convert string to array
        3) invert array order
        4) join array
    '''
    def reverse_words(self, s: str) -> str:
        array = s.split()
        array = array[::-1]
        return " ".join(array)
    
if __name__ == "__main__":
    solution = Solution()
    str1 = "a good   example"

    print(solution.reverse_words("the sky is falling"))
    print(solution.reverse_words("  hello world "))
    print(solution.reverse_words(str1))