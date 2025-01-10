pick = 0

def guess(num):
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0


class Solution:
    '''
        constriants:
        - 1 < number < n

        comments/questions for interviewer
        - N/A

        pseudo-code
        - bisectional guess approach, guess half way point of the range

        analysis
        - 
    '''
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n
        while True:
            current = round((higher - lower)/2) + lower
            res = guess(current)
            if res == 0:
                return current
            elif res > 0:
                lower = current + 1
            elif res < 0:
                higher = current - 1


if __name__ == "__main__":
    s = Solution()
    pick = 6
    print(s.guessNumber(10))

    pick = 1
    print(s.guessNumber(1))