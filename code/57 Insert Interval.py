# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        index1,index2=None,None
        flag=True
        for i in range(len(intervals)):
            tmp_start=intervals[i].start
            tmp_end=intervals[i].end
            if newInterval.start<=tmp_end and flag:
                index1=i
                flag=False
            if newInterval.end>=tmp_start:
                index2=i
        if index1 is None:
            return intervals+[newInterval]
        if index2 is None:
            return [newInterval]+intervals
        else:
            s=min(intervals[index1].start,newInterval.start)
            e=max(intervals[index2].end,newInterval.end)
            return intervals[:index1]+[Interval(s=s,e=e)]+intervals[index2+1:]