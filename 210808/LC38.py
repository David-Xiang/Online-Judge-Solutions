# LeetCode 38
# Count and Say
# String

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        last_str = self.countAndSay(n - 1)
        count = 1
        ans = []
        for i in range(1, len(last_str)):
            if last_str[i] != last_str[i - 1]:
                ans.append([count, last_str[i - 1]])
                count = 0
            count = count + 1
        ans.append([count, last_str[len(last_str) - 1]])
        return "".join([str(p[0]) + p[1] for p in ans])

if __name__ == "__main__":
    print(Solution().countAndSay(1))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(30))