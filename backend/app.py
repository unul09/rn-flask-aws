# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from model import ChatModel

app = Flask(__name__)
CORS(app)

chat_model = ChatModel()

@app.route('/users')
def users():
	# users 데이터를 Json 형식으로 반환한다
    return {"members": ["M1", "M2", "M3"]}

@app.route('/movies')
def movies():
    return {
  "title": "The Basics - Networking",
  "description": "Your app fetched this from a remote endpoint!",
  "movies": [
    { "id": "1", "title": "kimwonwoo", "releaseYear": "2001" },
    { "id": "2", "title": "james", "releaseYear": "1995" },
    { "id": "3", "title": "broady", "releaseYear": "2023" },
    { "id": "4", "title": "smith", "releaseYear": "2020" },
    { "id": "5", "title": "bye...", "releaseYear": "2014" }
  ]
}


@app.route('/hello')
def say_hello_world():
    return {'result': "Hello World"}


@app.route('/question', methods=['POST'])
def question():
    q = request.get_json()
    answer = chat_model.get_answer(q["text"])
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)