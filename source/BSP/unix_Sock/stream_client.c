#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    int fd, cl;
    char *buf={"fatti non foste per viver come bruti"};
    char buf2[128];
    struct sockaddr_un addr;

    memset(buf2, 0, 128);

    fd = socket(AF_UNIX, SOCK_STREAM, 0);

    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, "/tmp/serv_stream", sizeof(addr.sun_path)-1);

    connect(fd, (struct sockaddr*)&addr, sizeof(addr));

    while(1)
    {
        int t=0;
        int q = send(fd, buf, 37, 0);
        printf("q: %d\n", q);

        t=recv(fd,buf2,34, 0);
        printf("t:%d-->%s",t, buf2);
        sleep(1);
    }
    return 0;
}