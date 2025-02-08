'''
    Intuition:
    - The challenge involves in optimizing solution for the array spacing
    - change() specifies the specific index, makes this problem problematic
        - in brutal force, we can extend the array to the specified index size, however, this is a waste of space
    - Alternatively, we cannot use a single dictionary due to the find() function
    
    Approach:
    - Initialize the class with an array AND a dictionary
    - change() will fill the array with a array of a tuple containing both the index and 
'''
class NumberContainers:
    def __init__(self):
        self.nums = []


    def change(self, index: int, number: int) -> None:
        if index >= len(self.nums):
            return        
        self.nums[index] = number
        

    def find(self, number: int) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] == number:
                return i
        return -1


if __name__ == "__main__":
    s = NumberContainers()
    print(s.find(10))
    print(s.change(2, 10))
    print(s.change(1, 10))
    print(s.change(3, 10))
    print(s.change(5, 10))
    print(s.find(10))
    print(s.change(1, 20))
    print(s.find(10))