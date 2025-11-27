from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    if file:
        # Read the image
        input_image = Image.open(file.stream)
        # Remove background
        output_image = remove(input_image)
        # Save to bytes
        output_bytes = io.BytesIO()
        output_image.save(output_bytes, format='PNG')
        output_bytes.seek(0)
        return send_file(output_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)