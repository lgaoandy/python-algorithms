import heapq

class Solution:
    '''
        constriants:
        - n == nums1.length == nums2.length
        - 1 <= n < e5

        comments/questions for interviewer
        - greedy appraoch 

        pseudo-code
        - sort num1, num2 by num2
        - because we only care about the min value of num2, we can obtain the maximum score when num2 to equal to each value possible
        - from there, we only need to track the sum of num1

        analysis
        - time complexity: O(nlogn)
        - space complexity: O(k)
    '''
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # make an array of pairs (we want to sort both lists by num2)
        pairs = [ (n1, n2) for n1, n2 in zip(nums1, nums2) ]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            # calculate the sum from num1
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
        return res
            

if __name__ == "__main__":
    s = Solution()
    print(s.maxScore([1,3,3,2],[2,1,3,4],3))
    print(s.maxScore([4,2,3,1,1],[7,5,10,9,6],1))