from models.graph import Graph
from views.graph_view import GraphView

class GraphController:

    def __init__(self):
        self.graph = Graph()
        self.view = GraphView()

    def run(self):
        self.view.display_title("CAMPUSNET - ACADEMIC SOCIAL NETWORK")

        self.load_users()
        self.load_relationships()

        self.view.display_graph(self.graph)

        self.run_bfs_tests()
        self.run_dfs_test()
        self.run_social_queries()
        self.run_reachability_tests()
        self.run_crud_tests()

        self.view.display_title("FINAL GRAPH")
        self.view.display_graph(self.graph)

        print("\nTotal users:", len(self.graph.vertices))
        print(
            "Total relationships:",
            sum(len(edges) for edges in self.graph.adjacency_list.values())
        )

    def load_users(self):
        users = [
            ("U001", "Alex Restrepo", "student"),
            ("U002", "Sofia Calderon", "professor"),
            ("U003", "Daniel Zapata", "graduate"),
            ("U004", "Emma Garcia", "student"),
            ("U005", "Lucas Junior", "graduate"),
            ("U006", "Olivia Wilson", "professor"),
            ("U007", "Noah Tanaka", "student"),
            ("U008", "Mia Cepeda", "graduate"),
            ("U009", "Ethan Martinez", "student"),
            ("U010", "Isabella Saldarriaga", "professor"),
            ("U011", "James Rodriguez", "student"),
            ("U012", "William Osorio", "graduate")
        ]

        self.view.display_title("LOADING USERS")

        for user_id, name, role in users:
            success = self.graph.add_vertex(user_id, name, role)
            self.view.display_operation(
                f"Adding user {name}", success
            )

    def load_relationships(self):
        relationships = [
            ("U001", "U002"),
            ("U001", "U003"),
            ("U001", "U006"),
            ("U001", "U007"),

            ("U002", "U003"),
            ("U002", "U008"),
            ("U002", "U009"),
            ("U002", "U010"),

            ("U003", "U001"),

            ("U006", "U011"),
            ("U006", "U007"),

            ("U007", "U011"),
            ("U007", "U008"),

            ("U008", "U012"),
            ("U008", "U009"),

            ("U009", "U012"),
            ("U010", "U011"),

            ("U011", "U012"),
            ("U012", "U006")
        ]

        self.view.display_title("LOADING FOLLOW RELATIONSHIPS")

        for source_id, destination_id in relationships:
            success = self.graph.add_edge(source_id, destination_id)
            self.view.display_operation(
                f"{source_id} follows {destination_id}", success
            )

    def run_bfs_tests(self):
        self.view.display_title("BFS TESTS")

        for user_id in ["U001", "U006", "U004"]:
            self.view.display_bfs(self.graph, user_id)

    def run_dfs_test(self):
        self.view.display_title("DFS TEST")
        self.view.display_dfs(self.graph)

    def run_social_queries(self):
        self.view.display_title("SOCIAL NETWORK ANALYSIS")
        self.view.display_social_queries(self.graph)

    def run_reachability_tests(self):
        self.view.display_title("REACHABILITY TESTS")

        self.view.display_reachability(
            self.graph, "U001", "U012"
        )

        self.view.display_reachability(
            self.graph, "U004", "U012"
        )

    def run_crud_tests(self):
        self.view.display_title("CRUD OPERATIONS")

        success = self.graph.add_vertex(
            "U013", "Chris Anderson", "student"
        )
        self.view.display_operation("Create user U013", success)
        self.view.display_graph(self.graph)

        success = self.graph.add_edge("U013", "U004")
        self.view.display_operation(
            "Create relationship U013 -> U004", success
        )
        self.view.display_graph(self.graph)

        success = self.graph.update_vertex(
            "U013", name="Chris Rodriguez", role="graduate"
        )
        self.view.display_operation("Update user U013", success)
        self.view.display_graph(self.graph)

        success = self.graph.remove_edge("U013", "U004")
        self.view.display_operation(
            "Delete relationship U013 -> U004", success
        )
        self.view.display_graph(self.graph)

        success = self.graph.remove_vertex("U013")
        self.view.display_operation("Delete user U013", success)
        self.view.display_graph(self.graph)