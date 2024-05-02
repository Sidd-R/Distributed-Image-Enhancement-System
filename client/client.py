# implement socket client using socketio and take image input using tinkter
#  socket client docs : https://python-socketio.readthedocs.io/en/stable/client.html
import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("connection established")
    # a, b = map(int, input("enter two numbers: ").split())
    # sio.emit("math_req", {"a": a, "b": b})


@sio.on("res")
def update_clock(data):
    lamport_clock = data["clock"] 
    print(f"image process complted, lamport clock {lamport_clock}")


# @sio.on("math_res")
# def math_res(data):
#     print(f"addition result is {data[0]}")
#     print(f"substraction result is {data[1]}")
#     print(f"multiplication result is {data[2]}")
#     print(f"division result is {data[3]}")
#     print(f"power result is {data[4]}")


if __name__ == "__main__":
    lamport_clock = 0

    sio.connect("http://localhost:5000")
    img_path = "C:\\Users\\Siddhant Rao\\Desktop\\disrtibuted_computing_mpr\\server\\wumpus.jpeg"
    while True:
        x = int(input())

        if x == 0:
            break
        elif x == 1:
            sio.emit("process", {"img": img_path})

    sio.wait()
