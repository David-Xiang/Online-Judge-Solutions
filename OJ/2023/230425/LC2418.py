
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[t[0]] for t in sorted([i for i in enumerate(heights)], key = lambda t: t[1], reverse = True)]


if __name__ == '__main__':
    print(Solution().sortPeople(["Mary", "John", "Emma"],  [180, 165, 170]))
    print(Solution().sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
