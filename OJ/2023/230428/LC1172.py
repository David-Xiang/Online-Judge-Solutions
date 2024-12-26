from heapq import heappop, heappush


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.notEmpty = []
        self.notFull = []
        self.plates = dict()

    def push(self, val: int) -> None:
        if len(self.notFull) == 0:
            index = len(self.plates)
            self.plates[index] = []
            self.notFull.append(index)
        
        plate = self.notFull[0]
        self.plates[plate].append(val)
        if len(self.plates[plate]) == 1:
            heappush(self.notEmpty, -plate)
        if len(self.plates[plate]) == self.capacity:
            heappop(self.notFull)

    def pop(self) -> int:
        while len(self.notEmpty) > 0 and len(self.plates[-self.notEmpty[0]]) == 0:
            heappop(self.notEmpty)
        
        if len(self.notEmpty) == 0:
            return -1

        plate = -self.notEmpty[0]
        if len(self.plates[plate]) == self.capacity:
            heappush(self.notFull, plate)
        return self.plates[plate].pop()

    def popAtStack(self, index: int) -> int:
        if len(self.plates) - 1 < index or len(self.plates[index]) == 0:
            return -1
        if len(self.plates[index]) == self.capacity:
            heappush(self.notFull, index)
        return self.plates[index].pop()


if __name__ == "__main__":
    D = DinnerPlates(2)
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    print(D.popAtStack(0))
    D.push(20)
    D.push(21)
    print(D.popAtStack(0))
    print(D.popAtStack(2))
    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())
    print(D.pop())