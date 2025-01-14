class Solution:
    '''
        Constriants:
        - 1 <= A.lenght == B.length <= 50
        - 1 <= A[i], B[i] <= n
        - It is guaranteed that A and B are both permutation of n integers

        Comments/questions for interviewer
        - are the values in A and B always unique?

        Pseudo-code
        - semi-brute force run: iterate through A and B at the same time, adding to a set for each A and B
        - compare set A and B for common items and add to result

        Analysis
        - time complexity: O(n)
        - space complexity: O(3n)
    '''
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        numsA = set([A[0]])
        numsB = set([B[0]])
        res = [0] * n
        
        if A[0] == B[0]:
            res[0] = 1

        for i in range(1, n):
            numsA.add(A[i])
            numsB.add(B[i])
            count = 0
            if A[i] == B[i]:
                count += 1
            else:
                if A[i] in numsB:
                    count += 1
                if B[i] in numsA:
                    count += 1
            res[i] = res[i-1] + count
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
    print(s.findThePrefixCommonArray([2,3,1],[3,1,2]))