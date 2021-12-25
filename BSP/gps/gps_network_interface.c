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
#define _PORT                   1026
#define _MAXLINE                1024
#define clear()                 printf("\033[H\033[J")
#define _SENTENCTE_MAX_SIZE     1024


char *RMC;
char *GGA;
char *VTG;
char *GSA;
char *GSV1;
char *GSV2;
char *GSV3;
char *GSV4;
char *GSV5;
char *GGL;

int sockfd;
struct sockaddr_in servaddr, cliaddr;

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
	int fd = open("/dev/ttyS4", O_RDWR | O_NOCTTY | O_NDELAY);

	if (fd < 0) {
		printf("Error opening file: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	// Create new termios struc, we call it 'tty' for convention
    struct termios tty;
    memset(&tty, 0, sizeof tty);

    // Read in existing settings, and handle any error
    if(tcgetattr(fd, &tty) != 0) {
        printf("Error %i from tcgetattr: %s\n", errno, strerror(errno));
    }

    tty.c_lflag &= ~ECHO; // Disable echo
    tty.c_lflag &= ~ECHOE; // Disable erasure
    tty.c_lflag &= ~ECHONL; // Disable new-line echo

    if (tcsetattr(fd, TCSANOW, &tty) != 0) {
       printf("Error %i from tcsetattr: %s\n", errno, strerror(errno));
    }

    RMC=malloc(1024);
    GGA=malloc(1024);
    VTG=malloc(1024);
    GSA=malloc(1024);
    GSV1=malloc(1024);
    GSV2=malloc(1024);
    GSV3=malloc(1024);
    GSV4=malloc(1024);
    GSV5=malloc(1024);
    GGL=malloc(1024);

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
    char buffer[2048];
    int n = read(fd, buffer, 1024);

    if(n>1)
    {
        if(strstr(buffer, "RMC"))
        {
            memcpy(RMC, buffer, n);
            //fprintf(stderr, "\n(%d/%d) - %s\n",n,strlen(buffer), buffer);
        }
        if(strstr(buffer, "GGA"))
            memcpy(GGA, buffer, n);
        if(strstr(buffer, "VTG"))
            memcpy(VTG, buffer, n);
        if(strstr(buffer, "GSA"))
            memcpy(GSA, buffer, n);
        if(strstr(buffer, "GGL"))
            memcpy(GGL, buffer, n);

        memset(buffer,'\0',2048);

    }

}

char* build_data_to_send()
{
    char *data=malloc(2048);
    char*ptr = data;

    memcpy(data,RMC,strlen(RMC));
    ptr = data+ strlen(RMC);

    memcpy(ptr,GGA,strlen(GGA));
    ptr+=strlen(GGA);

    memcpy(ptr,VTG,strlen(VTG));
    ptr+=strlen(VTG);

    memcpy(ptr,GSA,strlen(GSA));
    ptr+=strlen(GSA);

    memcpy(ptr,GGL,strlen(GGL));

    return data;
}

int main (void)
{
    int fd, MAXLINE = 2;
	unsigned int cli_len=sizeof(cliaddr);
    char data_to_send[128];
    char buffer[2];

	//log_fd = open_log();

	fd=set_device();

    init_server();



	while(1){

        get_sentences(fd);

        if(recvfrom(sockfd, (char *)buffer, MAXLINE,  0, ( struct sockaddr *) &cliaddr, &cli_len)>0)
        {
            char *a=build_data_to_send();
            sendto(sockfd, (const char *)a, strlen(a),  0, (const struct sockaddr *) &cliaddr, cli_len);
            free(a);
        }

        memset(data_to_send, 0, 128);
		//write_log(log_fd,t,h,p);

        usleep(100);

	    };

	return 0;
}
