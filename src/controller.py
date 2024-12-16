from src import db
from src.model import User
from flask import request, jsonify
from flask_restful import Resource

class getRecords(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.json
        # Check if email already exists
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            return jsonify({"message": "email is required"}), 400
        # Create new user
        new_user = User(
            name=data["name"],
            email=data["email"],
            password=data["password"],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(
            {"message": "user added successfully", "user": new_user.to_dict()}
        )


class getSingleRecord(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": "user doesn't exist"}
        return jsonify([user.to_dict()])

    def put(self, id):
        data = request.json
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": "user doesn't exist"}, 404
        user.name = data["name"]
        user.email = data["email"]
        user.password = data["password"]
        db.session.commit()
        return jsonify({"message": "user added successfully", "user": user.to_dict()})

    def delete(self, id):
        data = request.json
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": "user doesn't exist"}, 404
        db.session.delete(user)
        db.session.commit()
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
