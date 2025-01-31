class Solution:
    '''
        Intuition
        -

        Greedy Approach
        - 
    '''
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort intervals by the start value
        intervals = sorted(intervals, key=lambda x: x[0])

        # start with the first interval on the list
        prev = intervals[0]
        removals = 0

        for i in range(1, len(intervals)):
            # if the next interval does not overlap, prev = next interval
            if prev[1] <= intervals[i][0]:
                prev = intervals[i]
            else:
                # if overlaps, keep the interval that ends first
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
                removals += 1
        return removals


if __name__ == "__main__":
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))
    print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))