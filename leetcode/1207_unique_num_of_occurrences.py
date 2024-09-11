from collections import Counter

class Solution():
    '''
        pseudo-code
        - use a hashmap to keep track of different values and their occurrences
            - or use Counter
        - convert hashmap values into an array, checking for unique occurrences
    '''
    def unique_occurrences(self, arr: list[int]) -> bool:
        occurrences = list(Counter(arr).values())
        return len(set(occurrences)) == len(occurrences)


if __name__ == "__main__":
    test = Solution()
    print(test.unique_occurrences([1,2,2,1,1,3]))
    print(test.unique_occurrences([1,2]))
    print(test.unique_occurrences([-3,0,1,-3,1,1,1,-3,10,0]))