from lm_model import client_model
from image_generator import TogetherImageGenerator

API_KEY = "8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02"
model = client_model()
response = model.create_slide(text = 'write me a prompt for image generation model, for a infographics about russian communist revolution, with very good details like in an encyclopedia')
slide_prompt = response.choices[0].message.content


print(slide_prompt)


generator = TogetherImageGenerator(API_KEY)
saved_path = generator.generate_image(prompt=slide_prompt, filename="1.png")
