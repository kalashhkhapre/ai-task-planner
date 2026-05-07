from app.services.providers.openai_provider import generate_response

class GoalAgent:

    @staticmethod
    def run(state):

        goal = state["goal"]

        prompt = f"""
        Analyze the following project goal.

        Goal:
        {goal}

        Refine and clarify the objective.
        """

        refined_goal = generate_response(prompt)

        return {
            "refined_goal": refined_goal
        }