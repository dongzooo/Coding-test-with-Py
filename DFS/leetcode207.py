import collections
from typing import List


class Solution:

	def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced, visited = set(), set()
        
        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            # graph[i]가 빈 경우(==선수과목이 없는 경우) -> 실행이 안 되고 True return
            # 나머지 경우: 선수과목을 불러옴, loop가 있을 경우, traced에 남아있어서 적발
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            
            visited.add(i)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
