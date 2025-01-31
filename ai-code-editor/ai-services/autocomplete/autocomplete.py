import openai

def get_autocomplete_suggestions(code: str) -> str:
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=code,
        max_tokens=50,
    )
    return response.choices[0].text