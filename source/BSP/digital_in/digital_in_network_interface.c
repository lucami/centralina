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
	fprintf(stderr,"\rfd: %d", fd);
    return fd;
}


int open_log(){
	int fd;
	fd = open("thp_log.txt",O_CREAT|O_RDWR|O_APPEND,S_IRWXU|S_IRWXG|S_IRWXO);
	if(fd == -1)
	{
		fprintf(stderr,"ERROR creating logfile\n");
	}
	else
	{
		dprintf(fd,"************************\n*********NEWRUN*********\n************************\n");
	}
	return fd;
}

void write_log(int fd, char* sentence){

	if(fd != -1)
	{
		dprintf(fd, "%s\n",sentence);
	}
}

void get_sentences(int fd)
{
    static uint8_t antibounce_time = 0;
    static uint8_t antibounce_value = 0;
    char value;
    read(fd, &digital_in_value, 1);
    fprintf(stderr, "\ndigital_in: %d", digital_in_value);

}

char* build_data_to_send()
{
    char* data=malloc(2);
    sprintf(data,"%c",digital_in_value);
    return data;
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
            char* a=build_data_to_send();
            sendto(sockfd, (const char *)&a, sizeof(uint8_t),  0, (const struct sockaddr *) &cliaddr, cli_len);
            free(a);
        }

		//write_log(log_fd,t,h,p);

        usleep(100);

	    };

	return 0;
}
