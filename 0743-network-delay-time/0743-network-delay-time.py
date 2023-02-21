class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time_mat[from][to] = time
        time_mat = [[0] * (n + 1) for _ in range(n + 1)]
        graph = collections.defaultdict(list)
        
        for time in times:
            time_mat[time[0]][time[1]] = time[2]
            graph[time[0]].append(time[1])
        
        dq = collections.deque([(k, 0)])
        # find[i - 1] = k노드부터 i노드까지 도달하는데 걸리는 최소 시간
        # find[i - 1] = -1 은 k노드부터 해당 i노드까지 도달하는 데 걸리는 시간을 발견 못한 것을 의미
        find = [-1] * n
        find[k - 1] = 0
        while dq:
            cur_node, cur_time = dq.popleft()
            
            for node in graph[cur_node]:
                total_time = cur_time + time_mat[cur_node][node]
                
                if find[node - 1] == -1:
                    find[node - 1] = total_time
                    dq.append((node, total_time))
                else:
                    if find[node - 1] > total_time:
                        find[node - 1] = total_time
                        dq.append((node, total_time))
                        
        for t in find:
            if t == -1:
                return -1
        
        return max(find)