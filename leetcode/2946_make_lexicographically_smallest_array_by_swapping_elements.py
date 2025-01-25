from collections import deque
from heapq import heapify, heappush, heappop

class Solution:
    '''
        Intuition
        - Essentially, there are different groupings of sorted arrays and their positions are always fixed as a part the sorted array

        Approach
        - Iterate original array, creating an array copy with tuples of its value and index
        - Then sort copy array by value in lexicographic order
        - Iterate sorted array, find all numbers within a limit of each other - we can call this a cluster
            
            - Dry run example
                - Original array: [5, 13, 1, 10, 2], limit = 3
                - Assign index to tuples: [(5,0), (13,1), (1,2), (10,3) (2,4)]
                - Sort by values: [(1,2), (2,4), (5,0), (10,3), (13,1)]
                - Iterate by cluster: 
                    - [(1,2), (2,4), (5,0)] belongs in one cluster
                    - Get the indexes in this cluster: {0,2,4}
                    - Assign array[0] = 1
                    - Assign array[2] = 2
                    - Assign array[4] = 5
                    - Result of this iteration: [1, 13, 2, 10, 5]
                - Iterate by cluster: 
                    - [(10,3), (13,1)] belongs in one cluster
                    - Get indexes in a set: {1,3}
                    - Assign array[1] = 10
                    - Assign array[3] = 13
                    - Result of this iteration: [1, 10, 2, 13, 5], which is the correct answer
        
        Time complexity: O(nlogn)
        Space complexity: O(n)
    '''
    def lexicographically_smallest_array(self, nums: list[int], limit: int) -> list[int]:
        q = []
        res = [0] * len(nums)
        
        for i, value in enumerate(nums):
            q.append((value, i))
        q = deque(sorted(q, key=lambda x: x[0]))
        
        while q:
            value, i = q.popleft()
            cluster = [value]
            indexes = [i]
            heapify(indexes)
            
            while q and abs(q[0][0] - cluster[-1]) <= limit:
                value, i = q.popleft()
                cluster.append(value)
                heappush(indexes, i)
            
            for i in range(len(cluster)):
                res[heappop(indexes)] = cluster[i]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lexicographically_smallest_array([1,5,3,9,8], 2))
    print(s.lexicographically_smallest_array([1,7,6,18,2,1], 3))
    print(s.lexicographically_smallest_array([1,7,28,19,10], 3))
    print(s.lexicographically_smallest_array([6,3,5,2,1], 1))