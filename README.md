# Background Remover API

A Flask-based API for removing backgrounds from images using the rembg library.

## Prerequisites

- Python 3.8 or higher

## Installation

### Windows

1. Install Python from [python.org](https://www.python.org/downloads/) if not already installed.

2. Open Command Prompt and navigate to the project folder.

3. Create a virtual environment:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```
   venv\Scripts\activate
   ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### macOS

1. Install Python using Homebrew or from [python.org](https://www.python.org/downloads/):

   ```
   brew install python
   ```

2. Open Terminal and navigate to the project folder.

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Linux

1. Install Python using your package manager (e.g., for Ubuntu):

   ```
   sudo apt update
   sudo apt install python3 python3-venv
   ```

2. Open Terminal and navigate to the project folder.

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```
   python app.py
   ```

2. The API will start on `http://localhost:5000`.

3. To remove background from an image, send a POST request to `http://localhost:5000/remove-bg` with the image file in the 'file' field.

   Example using curl:

   ```
   curl -X POST -F "file=@test/1.png" http://localhost:5000/remove-bg --output output.png
   ```

4. The response will be the processed image with background removed in PNG format.

## Testing

A test image is provided in the `test/` folder. You can use `test/1.png` to test the API.
