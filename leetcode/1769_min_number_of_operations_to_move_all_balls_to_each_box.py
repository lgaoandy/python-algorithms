class Solution:
    '''
        constriants:
        - 1 <= boxes.length <= 2000
        - boxes[i] is either '0' and '1'

        comments/questions for interviewer
        - the number of operations it takes to move a ball from i to j is always the distance j - i

        pseudo-code
        - dynamic programming approach
        - loop boxes once from right to left 
        - record in a list the operations to move all balls from the right of the current box to the current box
        - second loop, we record the same from the left side while obtaining the sum of the left and right

        analysis
        - time complexity - O(2n)
        - space complexity - O(3n)
    '''
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        left_operations = [0] * n
        right_operations = [0] * n
        results = [0] * n

        # track the amount of balls from the right
        right_balls = 1 if boxes[-1] == "1" else 0
        for i in range(n-2, -1, -1):
            right_operations[i] = right_operations[i+1] + right_balls
            right_balls += 1 if boxes[i] == "1" else 0

        # results of the leftmost box, is the right_operations of the same position (because no balls exists on the left)
        results[0] = right_operations[0]

        # in similiar operation, we loop from the left, adding to left_operation, but also obtaining the results
        left_balls = 1 if boxes[0] == "1" else 0
        for i in range(1, n):
            left_operations[i] = left_operations[i-1] + left_balls
            left_balls += 1 if boxes[i] == "1" else 0
            results[i] = left_operations[i] + right_operations[i]

        return results

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations("110"))
    print(s.minOperations("001011"))