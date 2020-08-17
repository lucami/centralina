#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main()
{
    int t,fd, cl;
    char buf[128];
    char *buf2={"ma per seguir virtude e canoscenza"};
    struct sockaddr_un addr;

    fd = socket(AF_UNIX, SOCK_STREAM, 0);

    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, "/tmp/serv_stream", sizeof(addr.sun_path)-1);

    bind(fd, (struct sockaddr*)&addr, sizeof(addr));

    listen(fd, 5);

    cl = accept(fd, NULL, NULL);
    t=read(cl,buf,128);
    printf("t: %d -->%s\n", t, buf);
    /*while(t=read(cl,buf,sizeof(buf))>0)
        printf("%d", t);*/
    t=write(fd, buf2, 34);
    printf("t: %d -->%s\n", t, buf);
    return 0;
}