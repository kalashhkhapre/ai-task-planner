from app.graph.dag_builder import DAGBuilder


class DAGBuilderAgent:

    @staticmethod
    def run(state):

        dependencies = state.get("dependencies", [])

        builder = DAGBuilder()
        execution_order = []
        dag_edges = []

        if dependencies:
            builder.build_graph(dependencies)
            execution_order = builder.execution_order()
            dag_edges = [
                {"from": dep, "to": item["task"]}
                for item in dependencies
                for dep in item["depends_on"]
            ]

        return {
            "execution_order": execution_order,
            "dag_edges": dag_edges
        }
