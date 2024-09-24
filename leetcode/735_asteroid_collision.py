class Solution:
    '''
        pseudo-code
        - use a stack to store the result of the asteroids
        - loop through asteroids, compt
    '''
    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in asteroids:
            if len(stack) > 0 and stack[-1] > 0 and i < 0:
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(i):
                    stack.pop()
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(i)
                if stack[-1] == abs(i):
                    stack.pop()
            else:
                stack.append(i)
        return stack

if __name__ == "__main__":
    test = Solution()
    print(test.asteroid_collision([5,10,-5]))
    print(test.asteroid_collision([8,-8]))
    print(test.asteroid_collision([10,2,-5]))
    print(test.asteroid_collision([-2,-1,1,2]))
    print(test.asteroid_collision([-2,-2,1,-2]))