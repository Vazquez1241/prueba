from flask import Flask, jsonify, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hellow, wordld")

@app.route('/user/<username>')
def get_user(username):
    user = {'username':username}
    return jsonify(user)

@app.route("/users", methods=["POST","GET"])
def creater_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    user = {'username':username, 'email':email}
    return jsonify(user)



if(__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0')