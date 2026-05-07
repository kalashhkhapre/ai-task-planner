from app.services.llm_service import LLMService


class DependencyAnalyzer:

    @staticmethod
    def analyze(tasks):

        tasks_text = "\n".join(
            [f"{i+1}. {task}" for i, task in enumerate(tasks)]
        )

        prompt = f"""
        You are an AI task dependency analyzer.

        Your job is to identify execution dependencies between tasks.

        IMPORTANT RULES:
        - Use ONLY the exact task names provided.
        - DO NOT create new tasks.
        - DO NOT rephrase task names.
        - DO NOT modify spelling or wording.
        - Every dependency MUST exactly match an existing task.
        - If a task has no dependency, return an empty list [].
        - Return ONLY valid JSON.
        - No explanations.
        - No markdown.

        Tasks:
        {tasks_text}

        Return format:
        [
            {{
                "task": "Task Name",
                "depends_on": ["Dependency Task"]
            }}
        ]
        """

        response = LLMService.generate(prompt)

        return response