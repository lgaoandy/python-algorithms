class Solution:
    '''
        Pseudo code
        1) convert str into array
        2) setup constant with no vowels 
        3) loop string with two pointers, one from start, one from end
        4) move left pointer to the right, and move right pointer to the left
            - if vowel is found, stay
            - if both pointers are on a vowel, swap
            - if left meets right, end loop
    '''
    def reverse_vowels(self, s: str) -> str:
        array = list(s)
        vowels = 'aeiouAEIOU'
        left, right = 0, len(array) - 1

        while left < right:
            if array[left] not in vowels:
                left += 1
            if array[right] not in vowels:
                right -= 1
            if array[left] in vowels and array[right] in vowels:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return "".join(array)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse_vowels("hello"))
    print(solution.reverse_vowels("leetcode"))