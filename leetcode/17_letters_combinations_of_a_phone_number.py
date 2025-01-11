# class Solution:
#     '''
#         Constriants:
#         - 

#         Comments/questions for interviewer
#         - 

#         Pseudo-code
#         - 

#         Analysis
#         - 
#     '''
#     def letterCombinations(self, digits: str) -> list[str]:
#         telephone = {
#             2: "abc", 3: "def", 4: "ghi", 5: "jkl",
#             6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
#         }

#         def combine(digits, combinations):
#             for digit in digits:
#                 for letters in telephone[digit]:
#                     for combination in combinations:
#                         combination.push(digit)

            

# if __name__ == "__main__":
#     s = Solution()
#     print(s.letterCombinations("23"))