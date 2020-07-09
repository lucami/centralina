#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <stdlib.h>
#include <stdint.h>
#include "server.h"

int init_server(char* socket_path, int* fd)
{
    struct sockaddr_un addr;
    if ( (*fd = socket(AF_UNIX, SOCK_DGRAM, 0)) == -1)
    {
        perror("socket error");
        exit(-1);
    }

    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    if (*socket_path == '\0')
    {
        *addr.sun_path = '\0';
        strncpy(addr.sun_path+1, socket_path+1, sizeof(addr.sun_path)-2);
    }
    else
    {
        strncpy(addr.sun_path, socket_path, sizeof(addr.sun_path)-1);
        unlink(socket_path);
    }

    if (bind(*fd, (struct sockaddr*)&addr, sizeof(addr)) == -1)
    {
        perror("bind error");
        exit(-1);
    }

}

int send_data(int fd, void* data, int datalen)
{
    int data_sent=0;
    int t=0;

    while(data_sent < datalen)
    {
        t=write(fd, data, (datalen - data_sent));
        data_sent+=t;
    }
}

uint16_t read_data(int fd, char* buf, int len)
{
    uint16_t data_in=0;
    int t;
    data_in=read(fd,buf ,len);
    printf("%s\n", buf);
    return data_in;
}