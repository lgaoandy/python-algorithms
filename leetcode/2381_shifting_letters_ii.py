import string

class Solution:
    '''
        constriants:
        - 1 <= s.length, shifts.length <= 5e4
        - shifts[i].length == 3 (always specifies start, end, shift forward or reverse)
        - 0 <= start <= end < s.length
        - 0 <= directions <= 1
        - s consists of lowercase letters

        comments/questions for interviewer
        - because there can be repeated substrings for shifts, it is inefficient to apply shifts directly to the string

        pseudo-code
        - I will write an array representing the shift value for each index
        - for example, if a shift is [0, 1, 1], I would add 1 to index 0 and 1, applying that shift value
        - we loop through shifts entirely, to obtain a shift array, then loop through s and apply the shift 

        analysis
        - time complexity: O(nm), m = length of shifts, n = length of string, this is very bad because it is a quadratic complexity
    '''
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift_values = [0] * n
        shifted_string = [0] * n

        for start, end, direction in shifts:
            for i in range(start, end + 1):
                shift_values[i] += 1 if direction == 1 else -1
        
        for i in range(n):
            # gets the index of the current letter after shifts
            j = string.ascii_lowercase.find(s[i]) + shift_values[i]
            
            # ensures index is between 0-26
            while j < 0:
                j += 26
            
            while j > 25:    
                j -= 26
            
            # apply shifts
            shifted_string[i] = string.ascii_lowercase[j]
        return "".join(shifted_string)


    '''
        points to improve
        - in the previous solution, we noticed the time complexity is quadratic when we create the shift_values array
        - we need a way to simplify of converting each shift from O(n) to O(1), because we must at least loop through every shift
        - for this reason, we cannot use a solution where we loop through every index in the range a shift is specified
        - but rather, if we save the endpoints for a shift, that would make it O(1)

        pseudo-code
        - loop through shift, recording the start and end of shifts by direction and the negation of the shift at the end of the index range
        - loop through s, apply shift and maintaining a shift value as we add or substract by the accumulative shift
    '''
    def shiftingLettersOptimized(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        accumulative_shift = [0] * n

        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            accumulative_shift[start] += shift
            if end + 1 < n:
                accumulative_shift[end + 1] -= shift

        results = []
        shift = 0
        for i in range(n):
            # add accumulative shift to current shift
            shift += accumulative_shift[i]

            # find the index of the current letter in the string
            index = string.ascii_lowercase.find(s[i])

            # apply shift and ensure that the index is 0-26
            new_index = index + shift

            while new_index < 0:
                new_index += 26
            while new_index > 25:
                new_index -= 26
            
            results.append(string.ascii_lowercase[new_index])
        return "".join(results)


if __name__ == "__main__":
    s = Solution()
    print(s.shiftingLettersOptimized("abc", [[0,1,0],[1,2,1],[0,2,1]]))
    print(s.shiftingLettersOptimized("dztz", [[0,0,0],[1,1,1]]))