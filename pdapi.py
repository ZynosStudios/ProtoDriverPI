from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from base64 import encodebytes
from PIL import Image

import os
import io


app = Flask(__name__)
api = Api(app)
UPLOAD_DIRECTORY = "api_uploaded_files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


def find_file(filename):
    if "/" in filename:
        abort(400)
    if not os.path.exists(os.path.join(UPLOAD_DIRECTORY, filename)):
        abort(404)


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img


class Ping(Resource):
    def get(self):
        return {"data": "Pong"}


class UploadImage(Resource):
    def post(self, filename):
        if "/" in filename:
            abort(400)

        if os.path.exists(os.path.join(UPLOAD_DIRECTORY, filename)):
            abort(409)

        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(request.data)

        return "File Created", 201


class UpdateImage(Resource):
    def put(self, filename):

        find_file(filename)
        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(request.data)

        return "File Created", 200


class DeleteImage(Resource):
    def delete(self, filename):

        find_file(filename)
        os.remove(os.path.join(UPLOAD_DIRECTORY, filename))


class GetImage(Resource):
    def get(self, filename):

        find_file(filename)
        return get_response_image(os.path.join(UPLOAD_DIRECTORY, filename))

class GetAllImages(Resource):
    pass

class DisplayImage(Resource):
    pass

class ClearDisplay(Resource):
    pass

api.add_resource(Ping, "/ping")
api.add_resource(UploadImage, "/uploadimage/<filename>")
api.add_resource(UpdateImage, "/updateimage/<filename>")
api.add_resource(DeleteImage, "/deleteimage/<filename>")
api.add_resource(GetImage, "/getimage/<filename>")
app.run(debug=True, port=5000)