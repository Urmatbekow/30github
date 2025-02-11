from pptx import Presentation
from pptx.util import Inches

prs = Presentation()

# Example: Create a title slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Lesson: The Industrial Revolution"
subtitle.text = "Engaging, modernized content"

# Create a content slide
content_slide = prs.slides.add_slide(prs.slide_layouts[1])
content_title = content_slide.shapes.title
content_title.text = "Key Points"

# Add bullet points from the LLM output
textbox = content_slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(4))
tf = textbox.text_frame
for line in slide_content.split('\n'):
    p = tf.add_paragraph()
    p.text = line
    p.level = 1

# Optionally, insert images
left = Inches(1)
top = Inches(3)
content_slide.shapes.add_picture('path_to_generated_image.jpg', left, top, height=Inches(2))

prs.save('lesson_presentation.pptx')
