from flask import Flask,render_template,Response
from camera import VidCamera

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

def gen_camera(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_camera(VidCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

