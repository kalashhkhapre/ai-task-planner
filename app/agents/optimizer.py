from app.graph.parallel_detector import ParallelTaskDetector


class OptimizerAgent:

    @staticmethod
    def run(state):

        dependencies = state.get("dependencies", [])

        parallel_groups = ParallelTaskDetector.detect_parallel_tasks(dependencies)

        optimized_tasks = [
            {
                "group": index + 1,
                "tasks": tasks
            }
            for index, tasks in enumerate(parallel_groups)
        ]

        return {
            "optimized_tasks": optimized_tasks,
            "parallel_groups": parallel_groups
        }
