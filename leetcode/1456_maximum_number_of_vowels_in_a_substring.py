class Solution():
    '''
        pseudo-code
        - fixed sliding window
        - initialize window with length of k
        - loop through str with sliding window, overriding max vowel count
    '''
    def max_vowels(self, s: str, k: int) -> int:
        count = 0

        for i in range(0, k):
            if s[i] in 'aeiou':
                count += 1

        max_count = count

        for i in range(k, len(s)):
            if s[i-k] in 'aeiou' and s[i] not in 'aeiou':
                count -= 1
            elif s[i-k] not in 'aeiou' and s[i] in 'aeiou':
                count += 1
                max_count = max(max_count, count)
                if max_count == k:
                    return max_count
        return max_count
            
    


if __name__ == "__main__":
    test = Solution()
    print(test.max_vowels("abciiidef", 3))
    print(test.max_vowels("aeiou", 2))
    print(test.max_vowels("leetcode", 3))