#include <iostream>
#include <sys/socket.h>//Socket function. int socket(int namespace, int style, int protocol)
#include <arpa/inet.h>
#include <cstring>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;


int makeSocket(unsigned int port);
int readFromClient(int filedes);//gets data from client


int main (void){
	int port = 9092;//just because it's over 9000
	int s = makeSocket(9092);		//	  _         _
	fd_set active_fd_set, read_fd_set;// <- don't know \_(x,x)_/
	sockaddr_in clientname;
	unsigned int size;

	if (listen(s, 1) < 0){ //I guess listen returns an error code.
		cout<<"error listening!\n";
		return -1;
	}

	FD_ZERO(&active_fd_set);
	FD_SET(s, &active_fd_set);


	cout<<"STARTING SERVER"<<endl;

	while(1){ //M4D L00PZ
		read_fd_set = active_fd_set;//I can now see why globals are a problem
		if(select(FD_SETSIZE, &read_fd_set,NULL,NULL,NULL) < 0){//select is a way to handle multiple connections. I'm guessing this statement turns it 'on'
			cout<<"ERROR iN SELECT!"<<endl;
			return -1;
		}
		for (int i = 0; i <FD_SETSIZE; i++){
			if (FD_ISSET (i, &read_fd_set)){
				if (i == s){
					int n;
					size = sizeof(clientname);
					n = accept(s, (struct sockaddr *) &clientname, &size);// establishes new socket, original socket stays listening for new connections. cant be used with udp
					if (n < 0){
						cout<<"ACCEPT ERROR\n";
						return -1;
					}
					fprintf(stderr, "Server: connect from host %s, port %hd,\n", inet_ntoa(clientname.sin_addr), ntohs(clientname.sin_port));
					FD_SET(n, &active_fd_set);//does this increase FD_SETSIZE?
				}
				else{	//data coming from already connected session
					if(readFromClient(i) < 0){
						close(i);
						FD_CLR (i, &active_fd_set);//Decrease FD_SETSIZE?
					}
				}
			}
		}
	}

	return 0;
}

int makeSocket (unsigned int port){
	int tcp = 0;//int used to define whether tcp or udp in socket()
	sockaddr a;
        sockaddr_in name;
        int sock = socket(PF_INET, SOCK_STREAM, tcp);// see #include <sys/socket.h>

        name.sin_family = AF_INET;
        name.sin_port = htons(9092);    //converts byte order from hostbyte order to network byte order
        name.sin_addr.s_addr = htonl (INADDR_ANY);//converts unsigned int netlong from network byte order to host byte order

        if (bind (sock, (struct sockaddr *) &name, sizeof (name)) < 0){
                cout<<"ERROR"<<endl;
        }

	return sock;
}

int readFromClient (int filedes){
	int bytes = 256;
	char buffer[bytes];
	int nbytes;

	nbytes = read(filedes, buffer, bytes);
	if (nbytes < 0){
		cout<<"error reading bytes!\n";
		return -2;
	}
	else if (nbytes == 0){
		return -1;	//end of file!
	}
	else{
		//Prints all incoming data up to a cap of 256 bytes
		fprintf(stderr, "Server: got message: `%s'\n", buffer);
		return 0;
	}
}
