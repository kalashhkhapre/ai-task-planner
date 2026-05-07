from app.services.llm_service import LLMService
from app.rag.retriever import retrieve_context

class TaskDecomposer:

    @staticmethod
    def decompose(goal: str):
        context = retrieve_context(goal)

        prompt = f"""
        You are an AI task decomposition assistant.

        Break the following goal into actionable tasks.

        Retrieved Knowledge:
        {context}

        User Goal:
        {goal}

        RULES:
        - Return ONLY valid JSON.
        - Do NOT number tasks.
        - Do NOT add explanations.
        - Each task should be concise.
        - Each task should be a string.

        Format:
        [
            "Task 1",
            "Task 2",
            "Task 3"
        ]
        """


        response = LLMService.generate(prompt)

        return response