import socket

HOST = ''    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connection complete")
while True:
    st = input("Enter str")
    enc = st.encode()
    s.sendall(enc)
    data = s.recv(1024)
s.close()
