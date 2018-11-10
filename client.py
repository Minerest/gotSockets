import socket
import ctypes
import curses
from time import sleep


def main():
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
    except Exception as e:
        print(e)


    HOST = ''    # The remote host
    PORT = 50004              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        print("Connection complete")
    except Exception as e:
        print("Error with socket, Error output: ")
        print(e)
        return
    while True:
        st = input("Enter str")
        enc = st.encode()
        s.sendall(enc)
        sleep(3)
        for i in range(100):
            data = s.recv(1024)
            if data:
                break
        if data:
            data = data.decode()
            print(data)
        else:
            s.close()
            return
main()