class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        while i<len(intervals):
            if intervals[i][1]>=newInterval[0]:
                if intervals[i][1]<newInterval[1]:
                    intervals[i][1]=newInterval[1]
            if i<len(intervals)-1 and intervals[i][1]>=intervals[i+1][0]:
                if intervals[i][1]<intervals[i+1][1]:
                    intervals[i][1]=intervals[i+1][1]
                intervals.pop(i+1)
            else:
                i+=1
        if not intervals:
            intervals.append(newInterval)
        return intervals