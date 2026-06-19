class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutea = minutes * (360/60)
        houra = hour * (360/12) + minutes/60 * (360/12)
        angle = abs(houra - minutea)
        if angle > 180:
            return 360 - angle
        return angle
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.angleClock(12, 30))
    print(s.angleClock(3, 30))
    print(s.angleClock(3, 15))