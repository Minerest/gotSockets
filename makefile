all:
	g++ server.cpp -o server.o
	g++ client.cpp -o client.o
clean:
	rm *.o a.out
