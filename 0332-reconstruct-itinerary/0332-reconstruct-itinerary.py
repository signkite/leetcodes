class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 일단 어휘순대로 탐색하고 모든 노드를 방문한게 아닌데
        # 더이상 갈 수 있는 티켓이 없다면 백트래킹
        
        # 티켓 그래프 구성
        graph = {}
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = [ticket[1]]
            else:
                graph[ticket[0]].append(ticket[1])
        
        # 티켓 그래프 어휘순으로 정렬
        for dpt in list(graph.keys()):
            graph[dpt].sort()
        
        # lexical 순대로 경로를 dfs
        # 티켓이 하나도 남지 않아있다면 결과 return
        def dfs(graph, path, dpt, is_first):
            # dpt로 부터 갈 티켓이 없는데
            # 그래프의 모든 티켓이 소모되었다면 해당 경로 반환
            # 다른 티켓이 남아있다면 None 반환
            if dpt not in graph or not graph[dpt]:
                empty = True
                for key in graph:
                    if graph[key]:
                        empty = False
                        break
                
                if empty:
                    return path.copy()
                else:
                    return None
            
            # dpt로부터 갈 수 있는 dst 탐색
            for i, dst in enumerate(graph[dpt].copy()):
                graph[dpt].remove(dst)
                path.append(dst)
                result = dfs(graph, path, dst, False)
                if result:
                    # None이 아닌 결과가 반환되었다면 정답을 탐색 완료했다는 것이므로
                    # 결과를 반환
                    return result
                graph[dpt].insert(i, dst)
                del path[-1]
                
        return dfs(graph, ['JFK'], 'JFK', True)
                
        