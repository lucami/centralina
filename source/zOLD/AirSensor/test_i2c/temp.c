#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <inttypes.h>

#define I2C_ADDR 0x76

uint32_t T1;
int32_t  T2,T3;

int set_device(){
	int fd = open("/dev/i2c-2", O_RDWR);
	
	if (fd < 0) {
		printf("Error opening file: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
		printf("ioctl error: %s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	
	return fd;
}

void start_device(int fd){

	char buffer[2];
	int rval=0;

	buffer[0]=0xF4;
	buffer[1]=0x27;

	rval = write(fd, buffer, 2);
	if(rval != 2)
	{
		fprintf(stderr, "error in write 0xF4 reg. Expected 2, read %d\n",rval);
		exit(EXIT_FAILURE);
	}
}



uint8_t read_reg(int fd, uint8_t reg){

	uint8_t buffer=reg;
	int rval = write(fd, &buffer, 1);
	if(rval != 1)
	{
		fprintf(stderr, "error in write 0xFA reg. Expected 1, read %d\n",rval);
		return 1;
	}

	read(fd, &buffer, 1);
	//printf("0x%02X\n", buffer);
	return buffer;
}

void get_T_comp_coeff(int fd){

	T1=read_reg(fd, 0x88);
	T1+=read_reg(fd, 0x89)<<8;

	T2=read_reg(fd, 0x8A);
	T2+=read_reg(fd, 0x8B)<<8;
	
	T3=read_reg(fd, 0x8C);
	T3+=read_reg(fd, 0x8D)<<8;

	//fprintf(stderr,"T1: %d\nT2: %d\nT3: %d\n", T1,T2,T3);
}

int32_t t_fine;
int32_t compensate_T(int32_t adc_T)
{
	int32_t var1, var2, T;
	var1 = ((((adc_T>>3) - ((int32_t)T1<<1))) * ((int32_t)T2)) >> 11;
	var2 = (((((adc_T>>4) - ((int32_t)T1)) * ((adc_T>>4) - ((int32_t)T1))) >> 12) *	((int32_t)T3)) >> 14;
       	t_fine = var1 + var2;
	T =(t_fine*5+128)>>8;
       	return T;
}


int main (void) {
	int fd;
	int rval=0;

	int32_t t=0;
	int32_t t_comp=0;
	
	int32_t a=0,b=0,c=0;

	fd=set_device();

	start_device(fd);
	get_T_comp_coeff(fd);

	a=read_reg(fd, 0xFA);
	b=(read_reg(fd, 0xFB));
	c=(read_reg(fd, 0xFC)) & 0xF0;
	
	t=c>>4 | b<<4 | a <<12;
	

	//printf("RAW Temp: %X\n",t);

	t_comp = compensate_T(t);
	printf("COMP T: %d.%d\n",t_comp/100,t_comp%100);
	
	return 0;
}
