class Solution:
    '''
        constriants:
        - 1 <= words.length <= 100
        - 1 <= words[i].length <= 30
        - only lowercase letters

        comments/questions for interviewer
        - can there be repeating words?
        
        pseudo-code
        - brute force: double loop through words to get all substrings

        analysis
        - time complexity: O(n)
        - space complexity: ~O(n)
    '''
    def stringMatching(self, words: list[str]) -> list[str]:
        n = len(words)
        results = set()

        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[i] in words[j]:
                        results.add(words[i])
                    if words[j] in words[i]:
                        results.add(words[j])
        return list(results)
    

    '''
        optimization
        - sorted() function has O(nlogn) time complexity
        - main loop iterates words once, each time reducing the amount of substrings to check, reducing the amount of steps
    '''
    def stringMatchingOptmized(self, words: list[str]) -> list[str]:
        # sort words by length (shorter words first)
        words.sort(key=len)
        answer = []

        # iterate over each word in the list
        # words can only be a substring of a larger word
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.stringMatching(["mass", "as", "hero", "superhero"]))
    print(s.stringMatching(["leetcode", "et", "code"]))
    print(s.stringMatching(["blue", "green", "bu"]))