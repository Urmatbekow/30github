from lm_model import client_model
from image_generator import TogetherImageGenerator

API_KEY = "8ed6a19ef7f4177fdb79eec1dab85eee9a4e6342147688a44f7c695535e56f02"
model = client_model()

#before prompt
base_beg_prompt = 'write me a prompt for image generation model, to draw an infographics with very good details like in an encyclopedia, you need to give the texts with intructions like pixel left right up and so on, about'


#key topic prompt
instruction_prompt = ''


#final instruction prompt
base_end_prompt = '. consider the fact that image generation models can not really write texts well, can not draw the explanation. The last 10 symbols of your response should be a unique a hash out of this prompt(you can use any symbol)'



#response = model.create_slide(text = 'write me prompt for image gen model to make pixel style night new york skyscrapers with a place to big square shape billboard' )#base_beg_prompt + instruction_prompt + base_end_prompt)
#slide_prompt = response.choices[0].message.content


#print(slide_prompt)


generator = TogetherImageGenerator(API_KEY)
saved_path = generator.generate_image(prompt= '')#slide_prompt[:-10], filename=f"{slide_prompt[-10:-2]}.png")
