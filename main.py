from lm_model import client_model


model = client_model()
response = model.create_slide(text = 'What are some fun things to do in New York?')
print(response.choices[0].message.content)