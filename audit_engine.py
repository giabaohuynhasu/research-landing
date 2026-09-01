from openai import OpenAI

SYSTEM_PROMPT = open(
    "prompts/system_prompt.md",
    encoding="utf-8"
).read()


class ThirdOrderAudit:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def audit(self, paper_text):

        response = self.client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": paper_text
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content
