class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {}

        for course1, course2 in prerequisites:
            if course1 in adj: adj[course1].append(course2)
            else: adj[course1] = [course2]

        visited = set()

        def search(node, visiting):
            if node in visited: return True
            if node not in adj: 
                visited.add(node)
                return True

            visiting.add(node)

            for neighbour in adj[node]:
                if neighbour in visiting:
                    return False
                if neighbour not in visited:
                    if not search(neighbour, visiting):
                        return False


            visiting.remove(node)
            visited.add(node)
            return True
            

        for i in range(numCourses):
            if not search(i, set()): return False

        return True