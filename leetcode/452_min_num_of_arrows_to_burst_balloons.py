class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])

        count = 1
        prev_arrow_range = points[0]
        for i in range(1, len(points)):
            if prev_arrow_range[1] < points[i][0]:
                count += 1
                prev_arrow_range = points[i]
            else:
                prev_arrow_range = [max(prev_arrow_range[0], points[i][0]), min(prev_arrow_range[1], points[i][1])]
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))