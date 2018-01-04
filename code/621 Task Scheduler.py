class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        '''
        1.最理想的情况：所有任务之间都没有间隔  就是len(tasks)
        2.其他情况：先找出最高频的任务 一共出现了M次
        没个任务之间至少间隔N
        然后频数等于最高频任务的个数MCT
        '''
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)