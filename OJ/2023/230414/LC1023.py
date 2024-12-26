from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.matchOne(q, pattern) for q in queries]
    
    def matchOne(self, query: str, pattern: str) -> bool:
        q, p = 0, 0
        while q < len(query):
            if query[q].islower():
                if p < len(pattern) and query[q] == pattern[p]:
                    p = p + 1
                q = q + 1
            else: # query[q] isupper
                if p < len(pattern) and query[q] == pattern[p]:
                    p, q = p + 1, q + 1
                else:
                    return False

        if p < len(pattern):
            return False
        return True

if __name__ == "__main__":
    print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
    print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
    print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))