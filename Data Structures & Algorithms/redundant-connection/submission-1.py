class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = {}
        for node1, node2 in edges:
            if node1 in adj: adj[node1].append(node2)
            else: adj[node1] = [node2]
            if node2 in adj: adj[node2].append(node1)
            else: adj[node2] = [node1]

        all_visited = set()
        self.cycle_nodes = set()

        def search(node, prev, currently_visited):
            currently_visited.append(node)
            all_visited.add(node)

            for neighbour in adj[node]:
                # found cycle !! as neighbour is in all_visited set but is different to previous node
                if neighbour in all_visited and neighbour != prev:
                    for i, value in enumerate(currently_visited):
                        if value == neighbour: self.cycle_nodes = set(currently_visited[i:])
                    
                # otherwise continue to search
                elif neighbour not in all_visited and neighbour != prev:
                    search(neighbour, node, currently_visited)
                
            currently_visited.pop()

        search(1, -1, [])

        result = []

        for node1, node2 in edges:
            if node1 in self.cycle_nodes and node2 in self.cycle_nodes: result = [node1, node2]
        
        return result

        