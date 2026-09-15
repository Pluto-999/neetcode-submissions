class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # to be a tree - 
            # 1. must be connected (i.e. no disconnected components)
            # 2. no cycles

        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for (node1, node2) in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        # 1. must be connected
        visited = set()
        visited.add(0)

        def connected_from_zero(node):    
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    connected_from_zero(neighbour)

        connected_from_zero(0)
        
        for node in adj_list:
            if node not in visited: return False

        
        # 2. no cycles
        visited = set()
        self.is_valid = True

        def no_cycles(node, prev):
            for neighbour in adj_list[node]:
                # found a cycle !
                if neighbour in visited and neighbour != prev:
                    self.is_valid = False
                    return
                elif neighbour not in visited:
                    visited.add(neighbour)
                    no_cycles(neighbour, node)
                
        visited.add(0)
        no_cycles(0, -1)
        return self.is_valid

