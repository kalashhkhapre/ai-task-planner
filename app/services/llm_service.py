from app.services.providers.openai_provider import generate_response


class LLMService:

    @staticmethod
    def generate(prompt: str):

        response = generate_response(prompt)

        return response