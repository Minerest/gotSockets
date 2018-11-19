#!/usr/bin/python
import sys #for command line args
import socket
#import ctypes
# from random import choices as randCho
# from string import ascii_uppercase
# from string import digits


class system:

    def __init__(self):
        self.host, self.port = self.configureConn()

    def configureConn(self):
        try:
            int(sys.argv[2])
            HOST, PORT = self.getCmd(sys.argv[1], sys.argv[2])
        except Exception as e:
            print(e)
            HOST, PORT = self.getConfigFile()
        return (HOST, int(PORT))

    def getConfigFile(self):
        # Gets the data within the ./config file.
        # The return is a tuple containing the HOST and PORT settings.
        with open("./config", 'r') as conf:
            data = conf.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip('\n')
        print(data)

        # This is an object called configs. config.ky = val
        # Step 1:get the length of the config file
        # Step 2: split each line in the data file at the ':'
        # step # step 3: set the split to a pair of variables ky and val.

        configs = {ky: val for ky, val in (data[x].split(':') for x in range(len(data)))}
        return (configs["HOST"], configs["PORT"])

    def getCmd(self):
        try:
            PORT = int(PORT)
        except:
            print("Invalid port, pick one greater than 10,000")
            sys.exit(1)
        if isPortCorrect(PORT):
            return (HOST, PORT)
        else:
            printHelp()
            sys.exit(1)
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.host, self.port))
            print("Connection complete")
        except Exception as e:
            print(e)
            sys.exit(1)

def main():
    # make the system class
    Syst = system()

    # get IP and PORT from command line or conf file
    Syst.configureConn()

    # start the socket connection
    Syst.connect()
    while True:
        st = input("Enter str")
        print(st)
        enc = st.encode()
        Syst.sock.sendall(enc)
        data = Syst.sock.recv(1024)
        if data:
            data = data.decode()
            print(data)
        else:
            Syst.sock.close()
            return


def isPortCorrect(PORT):
    if PORT < 10000 or PORT > 65000:
        return False
    return True

def printHelp():
    # Function that prints what the program expects from the command line
    print("Example: python3 127.0.0.1 10000")

main()