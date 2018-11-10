import socket
def main():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50004             # Arbitrary non-privileged port
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
            toSend = data.decode()
        except:
            pass
        if 'AAA' in toSend:
            toSend += " was recieved!!!"
            print(toSend)
            reply = "Thanks, your message was recieved!"
            soSend2 = reply.encode()
            conn.send(soSend2)
        else:
            print("WRONG FLAGs")
            conn.close()
            return

main()