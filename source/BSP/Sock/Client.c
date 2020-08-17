// Client side implementation of UDP client-server model
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <errno.h>

#define PORT     1025
#define MAXLINE 1024

extern int errno ;

// Driver code
int main() {
    fork();
    int sockfd;
    char buffer[MAXLINE];
    char *hello = "H";
    struct sockaddr_in     servaddr;

    // Creating socket file descriptor
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));

    // Filling server information
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    int n, len=sizeof(servaddr);

    sendto(sockfd, (const char *)hello, 17, 0, (const struct sockaddr *) &servaddr,sizeof(servaddr));
    printf("Hello message sent.\n");

    errno=0;
    memset(buffer,0,MAXLINE);
    n = recvfrom(sockfd, (char *)buffer, MAXLINE, 0, (struct sockaddr *) &servaddr, (socklen_t*) &len);
    buffer[n] = 0;
    printf("Server (%d) : %s\n", n, buffer);

    close(sockfd);
    return 0;
}