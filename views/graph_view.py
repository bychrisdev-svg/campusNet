class GraphView:

    @staticmethod
    def display_title(title):
        print("\n" + "=" * 55)
        print(f" {title}")
        print("=" * 55)

    @staticmethod
    def display_graph(graph):
        print("\n========== ADJACENCY LIST ==========")

        for user_id, connections in graph.adjacency_list.items():
            vertex = graph.vertices[user_id]
            followers = ", ".join(connections) if connections else "None"

            print(
                f"{user_id} | {vertex.name} ({vertex.role}) "
                f"-> [{followers}]"
            )

        print("====================================")

    @staticmethod
    def display_bfs(graph, start_id):
        result = graph.bfs(start_id)

        print(f"\nBFS starting at {start_id}:")
        print("Visit order:", " -> ".join(result))
        print("Vertices reached:", len(result))

    @staticmethod
    def display_dfs(graph):
        result = graph.dfs()

        print("\nDFS complete traversal:")
        print("Discovery order:", " -> ".join(result))
        print("Directed cycle detected:", graph.has_cycle())

    @staticmethod
    def display_social_queries(graph):
        print("\n========== SOCIAL QUERIES ==========")

        print("Users without followers:")
        for user_id in graph.users_without_followers():
            print(f"- {user_id}: {graph.vertices[user_id].name}")

        print("\nMost influential users:")
        for user_id in graph.most_influential():
            print(
                f"- {user_id}: {graph.vertices[user_id].name} "
                f"({graph.in_degree(user_id)} followers)"
            )

        print("\nMost active users:")
        for user_id in graph.most_active():
            print(
                f"- {user_id}: {graph.vertices[user_id].name} "
                f"({graph.out_degree(user_id)} following)"
            )

        print("====================================")

    @staticmethod
    def display_reachability(graph, source_id, destination_id):
        reachable = graph.can_reach(source_id, destination_id)

        print(
            f"\nCan {source_id} reach {destination_id}? "
            f"{'Yes' if reachable else 'No'}"
        )

    @staticmethod
    def display_operation(message, success):
        status = "SUCCESS" if success else "FAILED"
        print(f"\n[{status}] {message}")