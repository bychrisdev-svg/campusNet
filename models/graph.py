from collections import deque
from models.vertex import Vertex
from models.edge import Edge


class Graph:

    def __init__(self):
        self.vertices = {}
        self.adjacency_list = {}
        self.edges = []

    def add_vertex(self, user_id, name, role):

        if not user_id or not name:
            return False

        if user_id in self.vertices:
            return False

        if role not in ["student", "professor", "graduate"]:
            return False

        vertex = Vertex(user_id, name, role)

        self.vertices[user_id] = vertex
        self.adjacency_list[user_id] = []

        return True

    def remove_vertex(self, user_id):

        if user_id not in self.vertices:
            return False

        del self.vertices[user_id]
        del self.adjacency_list[user_id]

        for connections in self.adjacency_list.values():
            if user_id in connections:
                connections.remove(user_id)

        return True

    def update_vertex(self, user_id, name=None, role=None):

        if user_id not in self.vertices:
            return False

        if name is not None:
            if not isinstance(name, str) or not name.strip():
                return False
            self.vertices[user_id].name = name

        if role is not None:
            if role not in ["student", "professor", "graduate"]:
                return False
            self.vertices[user_id].role = role

        return True

    def add_edge(self, source_id, destination_id):

        if source_id not in self.vertices:
            return False

        if destination_id not in self.vertices:
            return False

        if destination_id in self.adjacency_list[source_id]:
            return False

        edge = Edge(source_id, destination_id)

        self.adjacency_list[source_id].append(edge.destination_id)

        return True

    def remove_edge(self, source_id, destination_id):

        if source_id not in self.adjacency_list:
            return False

        if destination_id not in self.adjacency_list[source_id]:
            return False

        self.adjacency_list[source_id].remove(destination_id)

        return True

    def bfs(self, start_id):

        if start_id not in self.vertices:
            return []

        visited = set()
        queue = deque([start_id])
        result = []

        visited.add(start_id)

        while queue:

            current = queue.popleft()
            result.append(current)

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self):

        visited = set()
        result = []

        def visit(current):

            visited.add(current)
            result.append(current)

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:
                    visit(neighbor)

        for user_id in self.vertices:

            if user_id not in visited:
                visit(user_id)

        return result

    def in_degree(self, user_id):

        if user_id not in self.vertices:
            return 0

        count = 0

        for connections in self.adjacency_list.values():
            if user_id in connections:
                count += 1

        return count

    def out_degree(self, user_id):

        if user_id not in self.vertices:
            return 0

        return len(self.adjacency_list[user_id])

    def users_without_followers(self):

        return [
            user_id
            for user_id in self.vertices
            if self.in_degree(user_id) == 0
        ]

    def most_influential(self):

        if not self.vertices:
            return []

        highest = max(
            self.in_degree(user_id)
            for user_id in self.vertices
        )

        return [
            user_id
            for user_id in self.vertices
            if self.in_degree(user_id) == highest
        ]

    def most_active(self):

        if not self.vertices:
            return []

        highest = max(
            self.out_degree(user_id)
            for user_id in self.vertices
        )

        return [
            user_id
            for user_id in self.vertices
            if self.out_degree(user_id) == highest
        ]

    def can_reach(self, source_id, destination_id):

        return destination_id in self.bfs(source_id)

    def has_cycle(self):

        visited = set()
        recursion_stack = set()

        def visit(current):

            visited.add(current)
            recursion_stack.add(current)

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:
                    if visit(neighbor):
                        return True

                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(current)
            return False

        for user_id in self.vertices:

            if user_id not in visited:
                if visit(user_id):
                    return True

        return False