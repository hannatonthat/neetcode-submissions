class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        times = self.timeMap[key]
        l, r = 0, len(times) - 1
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if timestamp < times[m][0]:
                r = m - 1
            else:
                res = times[m][1]
                l = m + 1
        return res