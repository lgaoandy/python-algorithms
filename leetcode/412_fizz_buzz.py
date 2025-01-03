class Solution:
    '''
        constriants:
        - sequence length: [1, e4]

        potential questions to ask interviewer
        - N/A

        pseudo-code
        - loop through the value given and generate output, using if conditions

        analysis
        - time complexity: O(n)
        - space complexity: O(n)
    '''
    def fizz_buzz(self, n: int) -> list[str]:
        result = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                result.append("FizzBuzz") 
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.fizz_buzz(3))
    print(s.fizz_buzz(5))
    print(s.fizz_buzz(15))