# socket server implementation using flask socketio
# flask socket io ddocs: https://flask-socketio.readthedocs.io/en/latest/getting_started.html
from rpc_client import RpcClient
import logging
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from PIL import Image
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dataclasses import dataclass
import time
from flask_cors import CORS,cross_origin


db = SQLAlchemy()


logging.basicConfig(
    filename="main_server.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
socketio = SocketIO(app)
CORS(app)

@dataclass
class User(db.Model):
    id: int
    username: str
    email: str
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
@dataclass
class Image(db.Model):
    id : int
    image_path: str
    processed_image_path: str
    # likes: int
    
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(120), unique=True, nullable=False)
    processed_image_path = db.Column(db.String(120), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # likes = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return "<Image %r>" % self.image_path
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

rpc = RpcClient(0)

lamport_clock = 0

# receive image from client 
@app.post("/process")
def process_image():
    file = request.files['image']
    temp_image_path = "./temp/uploaded_image.jpeg"
    file.save(temp_image_path)
    # rpc = RpcClient(lamport_clock)
    process_image_path = rpc.enhance_image(temp_image_path)
    return process_image_path
    
    # try:
    #     image = Image.open(file)
        


# @socketio.on("math_req")
# def handle_message(data):
#     print(f"received data a {data['a']} and b {data['b']}")
#     res = run(data['a'], data['b'])
#     socketio.emit("math_res", res)
    # send(res)
    
@socketio.on("process")
def process_image(data):
    print(f'Lamport clock at request received: {rpc.lamport_timestamp}')
    img_path = data['img']
    
    
    process_image_path = rpc.enhance_image(img_path)
    
    socketio.emit('res',{
        'clock': rpc.lamport_timestamp
    })
    print(f"Lamport clock request completed at {rpc.lamport_timestamp}")

@app.post("/image")
@cross_origin(supports_credentials=True)
def create_image():
    # receive form data with image and user id
    data = request.form
    user_id = data['user_id']
    file = request.files['image']
    temp_image_path = f"./temp/uploaded_image_{round(time.time())}.jpeg"
    file.save(temp_image_path)

    
    image = Image(image_path=temp_image_path, user_id=user_id)
    db.session.add(image)
    db.session.commit()
    return jsonify(image)

@app.get("/image")
def get_images():
    images = Image.query.all()
    print(images)
    return jsonify(images)
    

@app.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify(user)
    
    return jsonify({"error": "User not found"})

@app.post("/register")
def register():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user)

@app.post("/users")
def create_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user)

@app.get("/users")
def index():
    # users = User(username="user1", email="email1@em"), User(username="user2", email="email2@em")
    
    # db.session.add_all(users)
    # db.session.commit()
    # return jsonify(users)
    # return "ff"
    users = User.query.all()
    return jsonify(users)

if __name__ == "__main__":
    print("Main server is running on port: 5000")
    # socketio.run(app,debug=True)
    app.run(debug=True) 
    # socketio.run(app, host='0.0.0.0', debug=True)
    # with app.app_context():
        # db.create_all()
        
    # create users



    
    
