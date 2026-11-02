class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxfre = max(count.values())

        maxcount = 0
        for fre in count.values():
            if fre ==maxfre:
                maxcount += 1

        minTime = (maxfre - 1)*(n+1) + maxcount

        return max(len(tasks),minTime)


        