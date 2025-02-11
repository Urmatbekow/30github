from flask import Flask, request, send_file, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # A simple HTML form to upload images

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    file.save('uploaded.jpg')
    # Run steps 3-7 here
    return send_file('lesson_presentation.pptx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
