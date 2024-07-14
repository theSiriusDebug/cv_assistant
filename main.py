import os
from groq import Groq

class AI:
    def __init__(self):
        self.client = Groq()

    def read_file(self, file_path):
        with open(os.path.join(os.getcwd(), file_path), 'r') as file:
            return file.read()

    def generate_text(self, content):
        completion = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        for chunk in completion:
            for choice in chunk.choices:
                print(choice.delta.content or "", end="")

    def run(self, file1, file2):
        content = self.read_file(file1) + self.read_file(file2)
        self.generate_text(content)


if __name__ == "__main__":
    AI().run("config.txt", "job_description.txt")