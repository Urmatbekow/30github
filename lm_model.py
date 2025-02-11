
#8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02
from together import Together
#import openai

class client_model:
    def __init__(self):
        self.client = Together(TOGETHER_API_KEY = '8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02')

    def create_slide(self, text):
        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": f"{text}"}],
        )
