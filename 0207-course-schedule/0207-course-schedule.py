class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)
    
        checked = []  # 사이클이 없다고 확인이 완료된 노드는 재방문할 필요 없음
        visited = []  # 방문 경로 체크
        
        def dfs(dpt):
            if dpt in checked:
                return True
            elif dpt in visited:
                return False
            
            visited.append(dpt)
            for dst in graph[dpt]:
                # if dst in checked:
                #     continue
                # elif dpt in checked:
                #     return False
                
                if not dfs(dst):
                    return False
            
            checked.append(dpt)
            visited.remove(dpt)
            return True
        
        for start in list(graph.keys()):
            if not dfs(start):
                return False
        return True
        