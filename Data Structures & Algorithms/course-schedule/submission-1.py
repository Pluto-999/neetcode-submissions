class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = { i: [] for i in range(0, numCourses) }

        for course1, course2 in prerequisites:
            adj[course1].append(course2)

        
        def dfs(node, my_set):
            if node in my_set:
                return False
            if adj[node] == []:
                return True
            

            my_set.add(node)

            for neighbour in adj[node]:
                if not dfs(neighbour, my_set):
                    return False

            return True


        for i in range(0, numCourses):
            my_set = set()
            if not dfs(i, my_set):
                return False

        return True