from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask("Hawk REST API")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task', type=werkzeug.FileStorage, location='files')

class Analyse_IMG(Resource):
    def get(self):
        return "Use a POST Request: send image as `task` arguement"

    def post(self):
        args = parser.parse_args()
        image = args['task']
        image.save('received_file.png')
        return "Received the image!"

api.add_resource(Analyse_IMG, '/analyse')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12000)