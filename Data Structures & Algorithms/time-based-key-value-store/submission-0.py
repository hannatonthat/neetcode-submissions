class TimeMap:

    def __init__(self):
        self.time_map = {} # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        times = self.time_map.get(key, [])
        l, r = 0, len(times) - 1
        while l <= r:
            m = (r + l) // 2
            if times[m][1] <= timestamp:
                res = times[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
