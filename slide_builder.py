from pptx import Presentation
from pptx.util import Inches

def create_slide_deck(slides_content, output_file="presentation.pptx"):
    prs = Presentation()
    
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Your Presentation Title"
    subtitle.text = "Subtitle or Date"
