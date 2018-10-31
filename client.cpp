#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <cstring>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;

void writeToServer (int filedes);
void init_sockaddr(struct sockaddr_in *name, const char *hostname, unsigned short int port);
int main (void){
	srand(0);
/*	init_sockaddr(struct sockaddr_in *name,
				  const char *hostname,
				  unsigned short int port);*/
	int sock = socket(PF_INET, SOCK_STREAM, 0);
	struct sockaddr_in serverName;
	if (sock < 0){
		cout<<"Error making socket!"<<endl;
		return -1;
	}

	init_sockaddr (&serverName, "127.0.0.1", 9092);
	if (connect(sock, (struct sockaddr *) &serverName, sizeof(serverName)) < 0){
		cout<<"Error connecting to socket!"<<endl;
	}

	writeToServer (sock);
	close(sock);


	return 0;

}

void init_sockaddr(struct sockaddr_in *name, const char *hostname, unsigned short int port){

	struct hostent *hostinfo;
	name->sin_family = AF_INET;
	name->sin_port = htons (port);
	hostinfo = gethostbyname(hostname);
	if(hostinfo == NULL){
		cout<<"UNKNOWN HOST! EXITTING\n";
		return;
	}
	name->sin_addr = *(struct in_addr *) hostinfo->h_addr;



	return;
}

void writeToServer(int filedes){

	int nbytes;
	char str[256];
	bool running = true;
	int index = 0;
	while (running){
		cin>>str;	//I read that the ncurses library handles input without delay? I need to learn how I can send any other types of data. Maybe objects in json format?
/*		for (int i = 0; i < 256; i++){ trash data
			str[i] = rand()%26+47;
		}*/
		if(str[0] == '0') continue;
		nbytes = write(filedes, str , strlen(str) + 1);

		if (nbytes < 0){
			cout<<"ERROR, no bytes sent!"<<endl;
			return;
		}
	}
	return;
}
