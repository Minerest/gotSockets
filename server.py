import socket

def main():
    HOST, PORT = getConfig()
    # HOST = ''                 # Symbolic name meaning all available interfaces
    # PORT = 50004             # Arbitrary non-privileged port
    PORT = int(PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        print("Socket bound to port", PORT)
    except Exception as e:
        print("ERROR WITH SOCKET. Error output: ")
        print(e)
        return
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    i = 0
    while True:
        try:
            data = conn.recv(1024)
        except:
            data = ''
            print("EMPTY")
        i+=1
        print(data)
        dataDec = data.decode()
        if 'AAA' in dataDec:
            dataDec = dataDec.replace('AAA','')
            dataDec += " was recieved!!!"
            print(dataDec)
            reply = "Thanks, your message was recieved!"
            repEnc = reply.encode()
            conn.send(repEnc)
        elif 'exit' in dataDec or i == 50:
            print("Exit flag recieved")
            conn.close()
            s.listen(1)
            conn, addr = s.accept()
            print('Connected by', addr)

        else:
            print("Bad flags")
            reply = "Bad flags"
            repEnc = reply.encode()
            conn.send(repEnc)


def getConfig():
   #Gets the data within the ./config file.
   #The return is a tuple containing the HOST and PORT settings.

    #This gets the lines of a file 1 by 1.
   #The file is formatted with a ':' for key:value pairs
    with open("./config", 'r') as conf:
        data = conf.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip('\n')
    print(data)

   #This is an object called configs. config.ky = val
                                #        Step 1:get the length of the config file
                        #Step 2: split each line in the data file at the ':'
                #step 3: set the split to a pair of variables ky and val.
    configs = {ky:val for ky, val in (data[x].split(':') for x in range(len(data)))}

    return (configs["HOST"], configs["PORT"])
main()