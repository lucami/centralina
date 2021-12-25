#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <inttypes.h>
#include <sys/un.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <termios.h>

#define _BUF_LOG_SIZE           64
#define _PORT                   1028
#define _MAXLINE                1024
#define clear()                 printf("\033[H\033[J")
#define _SENTENCTE_MAX_SIZE     1024



int sockfd;
struct sockaddr_in servaddr, cliaddr;

uint8_t digital_in_value=0;

void init_server()
{
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Filling server information
    servaddr.sin_family    = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(_PORT);

    if ( bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0 )
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    fcntl(sockfd, F_SETFL, O_NONBLOCK);
}

int set_device(){
	int fd = open("/sys/class/gpio/gpio46/value", O_RDONLY| O_NOCTTY | O_NDELAY);
	fprintf(stderr,"\nfd: %d", fd);
    return fd;
}


void get_sentences(int fd)
{
    char path[100];
	char value_str[3];
	static int fd1;

	snprintf(path, 100, "/sys/class/gpio/gpio46/value");
	fd1 = open(path, O_RDONLY);
	if (-1 == fd1) {
		fprintf(stderr, "Failed to open gpio value for reading!\n");
	}

	if (-1 == read(fd1, value_str, 3)) {
		fprintf(stderr, "Failed to read value!\n");
	}

	close(fd1);
    digital_in_value=atoi(value_str);
    //fprintf(stderr, "\n\ndigital_in: %d", digital_in_value);
}

void build_data_to_send(char* data)
{
    memset(data,0,2);
    sprintf(data,"%d",digital_in_value);
    fprintf(stderr, "\n\ndigital_in: %d/%s", digital_in_value,data);
}

int main (void)
{
    int fd, MAXLINE = 2;
	unsigned int cli_len=sizeof(cliaddr);
    char buffer[2];

	fd=set_device();
    init_server();
    sleep(1);

	while(1){

        get_sentences(fd);
        if(recvfrom(sockfd, (char *)buffer, MAXLINE,  0, ( struct sockaddr *) &cliaddr, &cli_len)>0)
        {
            char a[2];
            build_data_to_send(a);
            sendto(sockfd, (const char *)a, 2,  0, (const struct sockaddr *) &cliaddr, cli_len);
        }
        //write_log(log_fd,t,h,p);
        usleep(1000);
    };

	return 0;
}
