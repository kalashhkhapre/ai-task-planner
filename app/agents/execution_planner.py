class ExecutionPlanner:

    @staticmethod
    def run(state):

        optimized_tasks = state.get("optimized_tasks", [])
        execution_order = state.get("execution_order", [])

        workflow_steps = [
            {
                "step": index + 1,
                "tasks": group["tasks"]
            }
            for index, group in enumerate(optimized_tasks)
        ]

        final_workflow = {
            "execution_order": execution_order,
            "workflow_steps": workflow_steps,
            "parallel_groups": optimized_tasks
        }

        return {
            "final_workflow": final_workflow
        }
