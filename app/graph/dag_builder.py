import networkx as nx

class DAGBuilder:

    def __init__(self):
        self.graph = nx.DiGraph()

    def build_graph(self, tasks):

        task_names = {item["task"] for item in tasks}

        for item in tasks:

            task = item["task"]

            self.graph.add_node(task)

            for dep in item["depends_on"]:

                if dep not in task_names:
                    raise ValueError(f"Dependency '{dep}' not found as a task")

                self.graph.add_edge(dep, task)

        return self.graph

    def execution_order(self):

        if nx.is_directed_acyclic_graph(self.graph):
            return list(nx.topological_sort(self.graph))

        raise Exception("Cycle detected in tasks")