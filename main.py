from lm_model import client_model
from image_generator import TogetherImageGenerator

API_KEY = "8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02"
model = client_model()

#before prompt
base_beg_prompt = 'write me a prompt for image generation model, to draw an infographics with very good details like in an encyclopedia about'

#key topic prompt
instruction_prompt = '1916 years genoside of kyrgyz population'

#final instruction prompt
base_end_prompt = '. consider the fact that image generation models can not really write texts well, can not draw the explanation. The last 5 symbols of your response should be a hash out of this prompt(you can use any symbol)'

response = model.create_slide(text =  base_beg_prompt + instruction_prompt + base_end_prompt)
slide_prompt = response.choices[0].message.content


print(slide_prompt)


generator = TogetherImageGenerator(API_KEY)
saved_path = generator.generate_image(prompt=slide_prompt[:-5], filename=f"{slide_prompt[-5:]}.png")
