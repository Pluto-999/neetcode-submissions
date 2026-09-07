class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = { n: [] for n in range(1, len(edges) + 1) }
        for (node1, node2) in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)


        def search(node, visited):

            visited.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    search(neighbour, visited)

        result = []

        for i in range(len(edges)):
            (node1, node2) = edges[i]
            
            adj[node1].remove(node2)
            adj[node2].remove(node1)
            
            visited = set()
            search(1, visited)

            if len(visited) == len(edges):
                result = [node1, node2]

            adj[node1].append(node2)
            adj[node2].append(node1)
            
        return result