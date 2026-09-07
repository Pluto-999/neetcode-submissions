class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {course: [] for course in range(numCourses)}

        for (course_1, course_2) in prerequisites:
            adj[course_1].append(course_2)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        result = []

        def search(node):
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False

            states[node] = VISITING

            for neighbour in adj[node]:
                if not search(neighbour):
                    return False

            states[node] = VISITED
            result.append(node)
            return True

        
        for course in range(numCourses):
            if not search(course):
                return []

        return result