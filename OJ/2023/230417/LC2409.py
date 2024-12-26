class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAliceIndex = self.dayIndex(arriveAlice)
        leaveAliceIndex = self.dayIndex(leaveAlice)
        arriveBobIndex = self.dayIndex(arriveBob)
        leaveBobIndex = self.dayIndex(leaveBob)
        intervalStart = max(arriveAliceIndex, arriveBobIndex)
        intervalEnd = min(leaveAliceIndex, leaveBobIndex)
        return intervalEnd - intervalStart + 1 if intervalStart <= intervalEnd else 0

    def dayIndex(self, date: str) -> int:
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month, day = map(lambda x: int(x), date.split('-'))
        index = sum(daysPerMonth[i] for i in range(month - 1)) + day
        return index


if __name__ == "__main__":
    print(Solution().countDaysTogether(arriveAlice="08-15",
          leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"))
    print(Solution().countDaysTogether(arriveAlice="10-01",
          leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"))
