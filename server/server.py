from flask import Flask, request, jsonify
from flask import Flask,render_template
import util

app = Flask(__name__, static_url_path="/static", static_folder='/Users/lostman/VS Code/Image_classifier/static')

@app.route('/')
def static_file():
    return app.send_static_file('app.html')
@app.route('/classify_image', methods=['GET', 'POST'])

def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)