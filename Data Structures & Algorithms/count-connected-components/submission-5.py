class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        
        visited = set()

        def search(node):
            queue = deque()
            queue.append(node)
            visited.add(node)

            while queue:
                first = queue.popleft()
                
                neighbours = adj_list[first]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            
        result = 0

        for node in adj_list:
            if node not in visited:
                result += 1
                search(node)

        return result