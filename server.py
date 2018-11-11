import socket

def main():
    HOST, PORT = getConfig()
    # HOST = ''                 # Symbolic name meaning all available interfaces
    # PORT = 50004             # Arbitrary non-privileged port
    PORT = int(PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        print("Scoket bount to port", PORT)
    except Exception as e:
        print("ERROR WITH SOCKET. Error output: ")
        print(e)
        return
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)

        try:
            print(data)
            dataDec = data.decode()
        except:
            conn.close()
            return
        if 'AAA' in dataDec:
            dataDec += " was recieved!!!"
            print(dataDec)
            reply = "Thanks, your message was recieved!"
            repEnc = reply.encode()
            conn.send(repEnc)
        else:
            print("WRONG FLAGs")
            conn.close()
            return

def getConfig():
   #Gets the data within the ./config file.
   #The return is a tuple containing the HOST and PORT settings.
    with open("./config", 'r') as conf:
        data = conf.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
    print(data)
    configs = {ky:val for ky, val in (data[x].split(':') for x in range(len(data)))}

    return (configs["HOST"], configs["PORT"])
main()