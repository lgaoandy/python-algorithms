import random

'''
    Requirement
    - All operations must have an average O(1) time complexity

    Intuition
    - Key component here is get random function, there are no ways to get a random value in a set or dictionary
        - e.g. random.choice(list(set)) would require O(n) time
    - To counteract this, we must store the value in a set/dictionary AND a list simultaneously
        - However, the problem arises for number removal
        - array.remove(item) is again O(n) time complexity
    - To counteract this, we can ask ourselves if there is a way to remove an item in array in O(1) time
        - there is, that is we swap the index of the item we seek to remove with the last index, then array.pop(), which is O(1) time
        - therefore, we must store the index of a number within the whole process, therefore, we must use a dictionary
'''
class RandomizedSet:
    def __init__(self):
        self.num_to_index = {}
        self.nums = []


    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False

        i = len(self.nums)
        self.nums.append(val)
        self.num_to_index[val] = i
        return True


    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        
        i = self.num_to_index[val]
        
        # swap with value at last index
        val2 = self.nums[-1]
        self.nums[i] = val2
        self.num_to_index[val2] = i

        # remove value
        self.nums.pop()
        del self.num_to_index[val]
        return True
    

    def getRandom(self) -> int:
        return random.choice(self.nums)



if __name__ == "__main__":

    s = RandomizedSet()
    print(s.insert(1))
    print(s.remove(2))
    print(s.insert(2))
    print(s.getRandom())
    print(s.remove(1))
    print(s.insert(2))
    print(s.getRandom())

    # print(s.insert(0))
    # print(s.insert(1))
    # print(s.remove(0))
    # print(s.insert(2))
    # print(s.remove(1))
    # print(s.getRandom())