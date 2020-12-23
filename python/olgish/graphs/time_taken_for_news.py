from  typing import List
import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time = {}
        for i, t in enumerate(informTime):
            time[i] = t
        
        manager_sub_ordinates = {}
        for empIndex in range(len(manager)):
            manager_sub_ordinates[empIndex] = [indx for (indx, m) in enumerate(manager) if empIndex == m]
            
        print(time)
        print(manager_sub_ordinates)
#     doing a bfs and at everylevel we take the maximim time taken at that level
        total_time_taken = 0
        q = [headID]
        while q:
            qsize = len(q)
            subs = []
            for _ in range(qsize):
                subs.append(q.pop(0))
            total_time_taken = total_time_taken + max([time.get(sub, 0) for sub in subs])
            for sub in subs:
                if sub != -1:
                    for ngh in manager_sub_ordinates[sub]:
                        q.append(ngh)

            print(q, max([time.get(sub, 0) for sub in subs]), total_time_taken)
            # print(total_time_taken)
        return total_time_taken


class Solution1:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
#     doing a bfs and at everylevel we take the maximim time taken at that level
        total_time_taken = 0
        q = [(headID, informTime[headID])]
        while q:
            node, time_taken_till =  q.pop(0)
            total_time_taken = max(total_time_taken, time_taken_till)
            for ngh in subordinates[node]:
                    q.append((ngh, time_taken_till + informTime[ngh]))
        return total_time_taken

# n  = 7
# headID = 6
# managers =  [1,2,3,4,5,6,-1]
# time_info = [0,6,5,4,3,2,1]

n = 11
headID = 4
managers =   [5,9,6,10,-1,8,9,1,9,3,4]
time_info =  [0,213,0,253,686,170,975,0,261,309,337]


sol = Solution()
print(sol.numOfMinutes(n, headID, managers, time_info))