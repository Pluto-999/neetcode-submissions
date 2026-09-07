class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = { node: [] for node in range(0, n) }

        for (node1, node2) in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        
        def search(node):

            visited[node] = True

            for neighbour in adj[node]:
                if visited[neighbour]:
                    continue
                search(neighbour)


        visited, result = [False] * n, 0
        
        for i in range(n):
            if not visited[i]:
                search(i)
                result += 1

        return result