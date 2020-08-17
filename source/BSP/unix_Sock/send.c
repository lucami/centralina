#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define DATA "The sea is calm tonight, the tide is full . . ."
#define NAME "socket"


/*
 * Send a datagram to a receiver whose name is specified in the command
 * line arguments.  The form of the command line is <program> <pathname>
 */


int main()
{
    int sock;
    struct sockaddr_un name;
    int buf=0;

    /* Create socket on which to send. */
    sock = socket(AF_UNIX, SOCK_DGRAM, 0);
    if (sock < 0)
    {
        perror("opening datagram socket");
        exit(1);
    }
    /* Construct name of socket to send to. */
    name.sun_family = AF_UNIX;
    strcpy(name.sun_path, NAME);
    /* Send message. */
    while(1){
        sendto(sock, DATA, sizeof(DATA), 0, (struct sockaddr *)&name, sizeof(struct sockaddr_un));
        sleep(2);
    }
    close(sock);
    return 0;
}