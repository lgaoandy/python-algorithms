class Solution:
    '''
        Approach
        - Sort the array
        - From the left to right, check for the maximum h index, we can use the current index and the size of citations to know how many papers are left
        - As soon as h index cannot be incremented, return h index, it is the maximum
    '''
    def hIndexSorting(self, citations: list[int]) -> int:
        ''' O(nlogn) time, O(sort) '''
        n = len(citations)
        index = 0
        citations.sort()

        for i in range(n):
            index = max(min(citations[i], n - i), index)
            if citations[i] > n - i:
                break
        return index


    def hIndexCounting(self, citations: list[int]) -> int:
        ''' O(n) time, O(n) space '''
        papers = len(citations)
        citation_buckets = [0] * (papers + 1)

        for citation in citations:
            citation_buckets[min(citation, papers)] += 1
        
        cumulative_papers = 0
        for h_index in range(papers, -1, -1):
            cumulative_papers += citation_buckets[h_index]
            if cumulative_papers >= h_index:
                return h_index


if __name__ == "__main__":
    s = Solution()
    print(s.hIndexCounting([3,0,6,1,5]))
    # print(s.hIndex([1,3,1]))
    # print(s.hIndex([100]))
    # print(s.hIndex([100, 200]))