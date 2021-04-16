from flask_restful import Resource
from flask_restful import reqparse


class Plus(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("x", type=int)
            parser.add_argument("y", type=int)
            args = parser.parse_args()

            result = args["x"] + args["y"]

            return {"result": result}
        except Exception as e:
            return {"error": str(e)}