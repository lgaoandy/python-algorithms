class Solution():
    '''
        pseudo-code
        - use a queue to simulate the voting
    '''
    def find_next_senator(self, senate: list[str], senator: str) -> int:
        for i in range(len(senate)):
            if senate[i] == senator:
                return i
        return -1
    
    def predict_party_victory(self, senate: str) -> str:
        queue = list(senate)
        
        while True:
            opposer = "D" if queue[0] == "R" else "R" # if queue[0] = R, opposor = D, etc.
            
            i = self.find_next_senator(queue, opposer)
            if i >= 1:
                queue.pop(i)
                queue.append(queue[0])
                queue.pop(0)
            else:
                return "Radiant" if queue[0] == "R" else "Dire"

if __name__ == "__main__":
    test = Solution()
    print(test.predict_party_victory("RD"))
    print(test.predict_party_victory("RDD"))