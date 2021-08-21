import os
from flask import Flask, jsonify, request 
from flask_cors import CORS
import base64
from MobileNet_KTH import test 
from movie import play_video
app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        # name = data.get('name', '')
        videodata = data.get('video', '')
        video_file = open('video.mp4','wb')
        decode_string = base64.b64decode(videodata)
        video_file.write(decode_string)
        prediction,maximum=test()
        play_video(prediction,maximum)
        # speakerRegister(name)
        return jsonify({'name':prediction}) 


if __name__=='__main__':
    app.run(debug=True)