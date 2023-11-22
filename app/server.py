from flask import Flask, jsonify, make_response, render_template, request 
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
    image.save('uploads/' + image.filename)

    return jsonify({'message': 'Image uploaded successfully', 'filename': image.filename})




if __name__ == '__main__': 
   app.run(debug = True)