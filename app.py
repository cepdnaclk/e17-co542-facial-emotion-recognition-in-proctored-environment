from flask import Flask, jsonify, make_response, render_template, request 
import preprocessor as pp
import predictor

app = Flask(__name__) 

@app.route('/') 
def index(): 
   return render_template('index.html') 

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    # You can customize the destination folder and filename as needed
    image_path = 'uploads/' + image.filename
    image.save(image_path)

    input_image = pp.process_image(image_path=image_path)

    emotion_weights = predictor.predict_emotion(image=input_image)

    return render_template('output.html', emotion_weights=emotion_weights)
    # return jsonify({'message': 'Image uploaded successfully', 'filename': image.filename})

if __name__ == '__main__':
   app.run(debug = True)