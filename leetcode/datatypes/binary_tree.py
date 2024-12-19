class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, num):
        if not self.val:
            self.val = num
        elif self.val < num:
            if self.right is None:
                self.right = TreeNode(num)
            else:
                self.right.insert(num)
        else: # self.val > num
            if self.left is None:
                self.left = TreeNode(num)
            else:
                self.left.insert(num)


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    
    def build(self, nums: list[int]):
        self.val = nums.pop(0)

        if len(nums) > 0:
            depth = 1
            nodes_of_depth = self._sum_powers_of_two(depth)
            left, right = [], []
            while len(nums) > 0:
                if len(left) < nodes_of_depth:
                    left.append(nums.pop(0))
                elif len(right) < nodes_of_depth:
                    right.append(nums.pop(0))
                else:
                    depth += 1
                    nodes_of_depth = self._sum_powers_of_two(depth)

            if len(left) > 0 and left[0] != None:
                self.left = TreeNode()
                self.left.build(left)
            if len(right) > 0 and right[0] != None:
                self.right = TreeNode()
                self.right.build(right)


    def _sum_powers_of_two(self, n: int) -> int:
        value = 0
        for i in range(n):
            value += pow(2, i)
        return value

            
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

