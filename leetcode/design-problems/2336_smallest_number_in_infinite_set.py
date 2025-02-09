import heapq

class SmallestInfiniteSet:
    '''
        constriants:
        - 1 <= num <= 1000

        comments/questions for interviewer
        - N/A

        pseudo-code
        - use a heap to implement
    '''
    def __init__(self):
        self.nums = [1,2]
        self.max = 2
        heapq.heapify(self.nums)


    def popSmallest(self) -> int:
        if len(self.nums) == 2:
            self.max += 1
            heapq.heappush(self.nums, self.max)
        return heapq.heappop(self.nums)


    def addBack(self, num: int) -> None:
        if num < self.max and num not in self.nums:
            heapq.heappush(self.nums, num)

    
    def getNums(self):
        return self.nums

    
if __name__ == "__main__":
    s = SmallestInfiniteSet()
    print(s.addBack(2))
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.addBack(1))
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.popSmallest())
    print(s.getNums())