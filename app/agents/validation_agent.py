from app.graph.dag_builder import DAGBuilder


class ValidationAgent:

    @staticmethod
    def run(state):

        dependencies = state.get("dependencies", [])

        report_lines = []
        builder = DAGBuilder()

        if not dependencies:
            report_lines.append("Warning: no dependencies found.")

        try:
            if dependencies:
                builder.build_graph(dependencies)
                builder.execution_order()
            report_lines.append("Validation passed: no cyclic dependencies detected.")
        except Exception as exc:
            report_lines.append(f"Validation failed: {exc}")

        return {
            "validation_report": "\n".join(report_lines)
        }
