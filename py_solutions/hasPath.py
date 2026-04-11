class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:        
        graph = {i: [] for i in range(n)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        
        visited = set()
        
        def dfs(src, dst):
            if src == dst: return True            
            visited.add(src)

            for neighbor in graph[src]:
                if neighbor not in visited:
                    if dfs(neighbor, dst):
                        return True
            return False

        return dfs(source, destination)



    
if __name__ == "__main__":
  s = Solution()
  graph = [
            [0,1],
            [1,2],
            [2,0]
            ]
  
  print(s.validPath(3, graph, 0, 2))
