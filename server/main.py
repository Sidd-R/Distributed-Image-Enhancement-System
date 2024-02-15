# socket server implementation using flask socketio
# flask socket io ddocs: https://flask-socketio.readthedocs.io/en/latest/getting_started.html
from rpc_client import run
import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, send

logging.basicConfig(
    filename="main_server.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on("math_req")
def handle_message(data):
    print(f"received data a {data['a']} and b {data['b']}")
    res = run(data['a'], data['b'])
    socketio.emit("math_res", res)
    # send(res)


if __name__ == "__main__":
    print("Main server is running on port: 5000")
    socketio.run(app,debug=True)
