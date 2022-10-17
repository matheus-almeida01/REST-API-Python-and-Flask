from importlib.metadata import requires
from flask_restful import Resource, reqparse
from models.usuario import UserModel
    
class User(Resource):
    
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message' : 'hotel not found'}, 404
    
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user(user_id)
            except:
                return {'message' : 'An error occurred trying to delete hotel'}, 500
            return {'message' : 'Hotel deleted'}
        return {'message' : 'Hotel not found'}, 404
    
    
