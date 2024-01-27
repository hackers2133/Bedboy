from flask import Flask, render_template
from flask_restful import Api, Resource
import ui

app = Flask(__name__)
api = Api(app)

class CameraPermissionResource(Resource):
    def get(self):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Camera Permission</title>
            <script>
                function requestCameraPermission() {
                    navigator.mediaDevices.getUserMedia({ video: true })
                        .then(function (stream) {
                            console.log('Camera access granted');
                            var videoElement = document.createElement('video');
                            videoElement.srcObject = stream;
                            document.body.appendChild(videoElement);

                            videoElement.addEventListener('click', function () {
                                stream.getTracks().forEach(track => track.stop());
                                videoElement.remove();
                            });
                        })
                        .catch(function (error) {
                            console.error('Camera access denied', error);
                        });
                }
            </script>
        </head>
        <body>
            <h1>Click the button to request camera access</h1>
            <button onclick="requestCameraPermission()">Allow Camera Access</button>
        </body>
        </html>
        """
        return ui.WebView(name='Camera Permission', html=html_content)

api.add_resource(CameraPermissionResource, '/camera_permission')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
