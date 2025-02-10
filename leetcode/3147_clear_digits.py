class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []
        for i in s:
            if i.isdigit() and len(ans) > 0:
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.clearDigits("abc"))
    print(s.clearDigits("cb34"))