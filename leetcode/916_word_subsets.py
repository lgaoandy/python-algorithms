import string

class Solution:
    '''
        Constriants:
        - all strings in word1 is unique
        - only lowercase letters

        Comments/questions for interviewer
        - is there a specific time and space complexity you are seeking?

        Pseudo-code
        - get a set of unique letters from words2
        - for each str in words1, make a letter dictionary of the letters seeking
        - for 

        Analysis
        - 
    '''
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        letters = {}

        # find the max occurrence requirement of each letter looping through words2
        # every str in word2 are not additives of each other but rather only maximum occurrence of each letter matters
        for word in words2:
            frequency = { i:0 for i in word }
            for i in word:
                frequency[i] += 1
            
            for i in frequency.keys():
                if i not in letters.keys():
                    letters[i] = frequency[i]
                else:
                    letters[i] = max(letters[i], frequency[i])
        
        res = []
        for word in words1:
            match = True
            # only check necessary letters required
            for sub in letters.keys():
                count = word.count(sub)

                # if a letter requirement fails, move onto next word
                if count < letters[sub]:
                    match = False
                    break

            # only append word if all letter requirements match
            if match:
                res.append(word)
        return res


    def countAos(self, aos):
        charCount = {}
        for string in aos:
            tempCount = {}
            for char in string:
                if char not in tempCount:
                    tempCount[char] = 0
                tempCount[char] = tempCount[char] + 1
           
            for key, value in tempCount.items():
                if key not in charCount:
                    charCount[key] = 0
                if charCount[key] < value:
                    charCount[key] = value
        return charCount
 

    def wordSubstring(self, str1, charCount):
        for key, value in charCount.items():
            if (str1.count(key) < value):
                return False
        return True
 

    def wordSubsetsEric(self, words1, words2):
        aos = self.countAos(words2)
        return filter(lambda value: self.wordSubstring(value, aos), words1)
       
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """

        
if __name__ == "__main__":
    s = Solution()
    print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","o"]))
    print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["l","e"]))
    print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["e","oo"]))
    print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["lo","eo"]))