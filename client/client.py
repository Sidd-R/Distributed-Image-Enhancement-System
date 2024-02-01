# implement socket client using socketio and take image input using tinkter
#  socket client docs : https://python-socketio.readthedocs.io/en/stable/client.html
import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("connection established")

    a, b = map(int, input("enter two numbers: ").split())

    sio.emit("math_req", {"a": a, "b": b})


@sio.on("math_res")
def math_res(data):
    print(f"addition result is {data[0]}")
    print(f"substraction result is {data[1]}")
    print(f"multiplication result is {data[2]}")
    print(f"division result is {data[3]}")
    print(f"power result is {data[4]}")


if __name__ == "__main__":
    sio.connect("http://localhost:5000")
    sio.wait()
