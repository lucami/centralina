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
#define _PORT                   1027
#define _MAXLINE                1024
#define clear()                 printf("\033[H\033[J")
#define _SENTENCTE_MAX_SIZE     1024


char* air_sensor_frame;
uint16_t pm10;
uint16_t pm2p5;
uint16_t frame_len;
uint16_t checksum;

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
	int fd = open("/dev/ttyS0", O_RDWR | O_NOCTTY | O_NDELAY);
    char command_buffer[4];
    int n;

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

    air_sensor_frame=malloc(1024);

    command_buffer[0]=0x68;
    command_buffer[1]=0x01;
    command_buffer[2]=0x02;
    command_buffer[3]=0x95;

    fprintf(stderr, "\r\nSending stop command...");

    sleep(2); //required to make flush work, for some reason
    tcflush(fd,TCIOFLUSH);


    n=write(fd, command_buffer, 4);
    memset(command_buffer,0,4);
    sleep(2);
    n = read(fd, command_buffer, 2048);
    fprintf(stderr, "   received %X %X ", command_buffer[0],command_buffer[1]);

    command_buffer[0]=0x68;
    command_buffer[1]=0x01;
    command_buffer[2]=0x40;
    command_buffer[3]=0x57;

    fprintf(stderr, "\r\nSending autosend command...");
    n=write(fd, command_buffer, 4);
    memset(command_buffer,0,4);
    sleep(2);
    n = read(fd, command_buffer, 4);
    fprintf(stderr, "   received %X %X ", command_buffer[0],command_buffer[1]);

    command_buffer[0]=0x68;
    command_buffer[1]=0x01;
    command_buffer[2]=0x01;
    command_buffer[3]=0x96;

    fprintf(stderr, "\r\nSending start command...");
    n=write(fd, command_buffer, 4);
    memset(command_buffer,0,4);
    sleep(2);
    n = read(fd, command_buffer, 4);
    fprintf(stderr, "   received %X %X ", command_buffer[0],command_buffer[1]);

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

void get_sentence(int fd)
{
    int n = read(fd, air_sensor_frame, 2048);
    int frame_ok = 1;
    uint16_t local_frame_len=0,local_pm2p5=0,local_pm10=0;

    if(n>1)
    {
        local_frame_len = air_sensor_frame[2]<<8 | air_sensor_frame[3];
        //fprintf(stderr, "\nframe_len: %X\n",local_frame_len);
        if(local_frame_len != 0x1C )
            frame_ok = 0;

        local_pm2p5 = air_sensor_frame[6]<<8 | air_sensor_frame[7];
        local_pm10 = air_sensor_frame[8]<<8 | air_sensor_frame[9];

        if(local_pm2p5 > local_pm10)
            frame_ok = 0;

        fprintf(stderr, "\npm2p5: %d - pm10: %d\n",local_pm2p5,local_pm10);
        //fprintf(stderr, "\n(%d/%d) - %s\n",n,strlen(air_sensor_frame), air_sensor_frame);
        memset(air_sensor_frame,'\0',2048);

        if(frame_ok == 1)
        {
            pm10 = local_pm10;
            pm2p5 = local_pm2p5;
        }
    }
}

char* build_data_to_send()
{
    char *data=malloc(2048);
    char *ptr = data;

    return data;
}

int main (void)
{
    int fd, MAXLINE = 2;
	unsigned int cli_len=sizeof(cliaddr);
    char data_to_send[128];
    char buffer[2];
    int data_len;
	fd=set_device();

    init_server();



	while(1){

        get_sentence(fd);
        data_len=sprintf(data_to_send, "%d;%d",pm2p5, pm10);
        int r = recvfrom(sockfd, (char *)buffer, MAXLINE,  0, ( struct sockaddr *) &cliaddr, &cli_len);
        fprintf(stderr, "\rr: ", r);
        if(r>0)
        {
            fprintf(stderr, "\rReceived trigger... Sending data...");
            sendto(sockfd, (const char *)data_to_send, strlen(data_to_send),  0, (const struct sockaddr *) &cliaddr, cli_len);
            fprintf(stderr, "\rSent: %s (%d)", data_to_send,strlen(data_to_send));
        }

        memset(data_to_send, 0, 128);

        usleep(100);

	    };

	return 0;
}
