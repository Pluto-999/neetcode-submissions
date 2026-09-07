class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {num: [] for num in range(n)}

        for (node1, node2) in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        
        visited = set()
        result = 0

        def search(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                search(nei)

        for num in range(n):
            if num not in visited:
                result += 1
                search(num)

        return result
        