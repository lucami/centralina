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
#define _BUF_LOG_SIZE 64 

uint32_t T1;
int32_t  T2,T3;

uint16_t P1;
int16_t P2,P3,P4,P5,P6,P7,P8,P9;

uint8_t H1,H3,H6;
int16_t H2,H4,H5;

#define clear() printf("\033[H\033[J")

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
	
	buffer[0]=0xF5;//registro config
	buffer[1]=0x05<<5;//t_standby a 1 secondo

	rval = write(fd, buffer, 2);
	if(rval != 2)
	{
		fprintf(stderr, "error in write 0xF2 reg. Expected 2, read %d\n",rval);
		exit(EXIT_FAILURE);
	}


	buffer[0]=0xF2;//registro umidita'
	buffer[1]=0x01;//oversampling x8

	rval = write(fd, buffer, 2);
	if(rval != 2)
	{
		fprintf(stderr, "error in write 0xF2 reg. Expected 2, read %d\n",rval);
		exit(EXIT_FAILURE);
	}

	buffer[0]=0xF4;//registro temperatura e pressione
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

void get_H_comp_coeff(int fd){

	H1=read_reg(fd, 0xA1);

	H2=read_reg(fd, 0xE1);
	H2+=read_reg(fd, 0xE2)<<8;
	
	H3=read_reg(fd, 0xE3);
	
	H4=read_reg(fd, 0xE4)<<4;
	H4+=(read_reg(fd, 0xE5)&0x0F);
	
	H5=read_reg(fd, 0xE5)&0xF0;
	H5+=read_reg(fd, 0xE6)<<4;
	
	H6+=read_reg(fd, 0xE7);

}

void get_P_comp_coeff(int fd){

	P1=read_reg(fd, 0x8E);
	P1+=read_reg(fd, 0x8F)<<8;

	P2=read_reg(fd, 0x90);
	P2+=read_reg(fd, 0x91)<<8;
	
	P3=read_reg(fd, 0x92);
	P3+=read_reg(fd, 0x93)<<8;
	
	P4=read_reg(fd, 0x94);
	P4+=read_reg(fd, 0x95)<<8;

	P5=read_reg(fd, 0x96);
	P5+=read_reg(fd, 0x97)<<8;
	
	P6=read_reg(fd, 0x98);
	P6+=read_reg(fd, 0x99)<<8;
	
	P7=read_reg(fd, 0x9A);
	P7+=read_reg(fd, 0x9B)<<8;

	P8=read_reg(fd, 0x9C);
	P8+=read_reg(fd, 0x9D)<<8;
	
	P9=read_reg(fd, 0x9E);
	P9+=read_reg(fd, 0x9F)<<8;

}

int32_t t_fine=0;
int32_t compensate_T(int32_t adc_T){
	int32_t var1, var2, T;
	var1 = ((((adc_T>>3) - ((int32_t)T1<<1))) * ((int32_t)T2)) >> 11;
	var2 = (((((adc_T>>4) - ((int32_t)T1)) * ((adc_T>>4) - ((int32_t)T1))) >> 12) *	((int32_t)T3)) >> 14;
       	t_fine = var1 + var2;
	T =(t_fine*5+128)>>8;
       	return T;
}



uint32_t compensate_P(int32_t adc_P)
{
	int64_t var1, var2, p;
	var1 = ((int64_t)t_fine)-128000;
	var2 = var1 * var1 * (int64_t)P6;
	var2 = var2 + ((var1*(int64_t)P5)<<17);
	var2 = var2 + (((int64_t)P4)<<35);
	var1 = ((var1 * var1 * (int64_t)P3)>>8) + ((var1 * (int64_t)P2)<<12);
       	var1 = (((((int64_t)1)<<47)+var1))*((int64_t)P1)>>33;
	if (var1 == 0)
	{
		return 0; // avoid exception caused by division by zero 
	}
	p = 1048576-adc_P;
	p = (((p<<31)-var2)*3125)/var1;
	var1 = (((int64_t)P9) * (p>>13) * (p>>13)) >> 25; 
	var2 = (((int64_t)P8) * p) >> 19;
	p = ((p + var1 + var2) >> 8) + (((int64_t)P7)<<4);
	return (uint32_t)p;
}



// Returns humidity in %RH as unsigned 32 bit integer in Q22.10 format 
// (22 integer and 10 fractional bits). 
// Output value of “47445” represents 47445/1024 = 46.333 %RH
uint32_t compensate_H(int32_t adc_H) {

    int32_t v_x1_u32r;
    v_x1_u32r = (t_fine-((int32_t)76800));
    v_x1_u32r = (((((adc_H << 14)-(((int32_t)H4) << 20)-(((int32_t)H5) * v_x1_u32r)) +((int32_t)16384)) >> 15) * (((((((v_x1_u32r * ((int32_t)H6)) >> 10) * (((v_x1_u32r * ((int32_t)H3)) >> 11) + ((int32_t)32768))) >> 10) + ((int32_t)2097152)) * ((int32_t)H2) + 8192) >> 14));
    v_x1_u32r = (v_x1_u32r-(((((v_x1_u32r >> 15) * (v_x1_u32r >> 15)) >> 7) * ((int32_t)H1)) >> 4)); 
    v_x1_u32r = (v_x1_u32r < 0 ? 0 : v_x1_u32r);
    v_x1_u32r = (v_x1_u32r > 419430400 ? 419430400 : v_x1_u32r);
    return (uint32_t)(v_x1_u32r>>12);
}



int32_t read_T_regs(int fd){

	int32_t a=0, b=0, c=0;

	a=read_reg(fd, 0xFA);
	b=(read_reg(fd, 0xFB));
	c=(read_reg(fd, 0xFC)) & 0xF0;
	
	int32_t t = c>>4 | b<<4 | a <<12;
	return t;
}	

int32_t read_P_regs(int fd){

	uint8_t a=0, b=0, c=0;

	a=read_reg(fd, 0xF7);
	b=(read_reg(fd, 0xF8));
	c=(read_reg(fd, 0xF9)) & 0xF0;
        
	int32_t p = a<<12 | b<<4 | c>>4;
	return p;
}	

int32_t read_H_regs(int fd){

	int32_t a=0, b=0;

	a=read_reg(fd, 0xFD);
	b=read_reg(fd, 0xFE);
	
	int32_t t = b | a<<8;
	return t;
}	

int32_t get_T(int fd){
	
	int32_t t = read_T_regs(fd);
	return compensate_T(t);
}

int32_t get_H(int fd){

	int32_t h = read_H_regs(fd);
	return compensate_H(h);
}

uint32_t get_P(int fd){
	int32_t p = read_P_regs(fd);
	return  compensate_P(p);
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

void write_log(int fd, int32_t t, int32_t h, uint32_t p){
	
	if(fd != -1)
	{
		dprintf(fd, "%d.%d,%f,%d.%d\n",t/100,t%100,h/1024.0,(p/256)/100,(p/256)%100);
	}
}

int main (void) {
	int fd,log_fd;
	int32_t t=0,h=0;
	uint32_t p=0;

	log_fd = open_log();

	fd=set_device();
	start_device(fd);
	
	get_T_comp_coeff(fd);
	get_H_comp_coeff(fd);
	get_P_comp_coeff(fd);
	
	sleep(5);

	while(1){
		clear();
		t=get_T(fd);
		h=get_H(fd);
		p=get_P(fd);
		printf("T: %d.%d\n",t/100,t%100);
		printf("H: %f\n",h/1024.0);
		printf("P: %d.%d\n",(p/256)/100, (p/256)%100);
		write_log(log_fd,t,h,p);
		sleep(2);
	}

	return 0;
}

