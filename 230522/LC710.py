import random
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        blackset = set(blacklist)
        swap_list = [i for i in blacklist if i < n - m]
        self.swap_map = {}
        j = n - m
        for i in swap_list:
            while j in blackset:
                j = j + 1
            self.swap_map[i] = j
            j = j + 1
        self.n = n - m

    def pick(self) -> int:
        num = random.randint(0, self.n - 1)
        return self.swap_map.get(num, num)
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

if __name__ == '__main__':
    obj = Solution(7, [2, 3, 5])
    print(obj.pick())
    print(obj.pick())
    print(obj.pick())
    print(obj.pick())
    print(obj.pick())
    print(obj.pick())
