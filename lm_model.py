import openai

class model:
    def __init__():
        self.response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts textbook content into engaging slide content."}
                #{"role": "user", "content": extracted_text}
            ]
        )

    def create_slide(self, text):
    slide_content = self.response['choices'][0]['message']['content']
    return slide_content
