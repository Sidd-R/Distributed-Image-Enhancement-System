# socket server implementation using flask socketio
# flask socket io ddocs: https://flask-socketio.readthedocs.io/en/latest/getting_started.html
from rpc_client import run
import logging

logging.basicConfig(
    filename="main_server.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

if __name__ == "__main__":
    res = run(10, 5)

    print(f"addition result is {res[0]}")
    print(f"substraction result is {res[1]}")
    print(f"multiplication result is {res[2]}")
    print(f"division result is {res[3]}")
    print(f"power result is {res[4]}")
