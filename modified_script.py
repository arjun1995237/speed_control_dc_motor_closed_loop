import  serial
import struct
from time import sleep
#list=[]
#length_list=0
#with open("/home/arjun/Desktop/piano.txt") as f:
#    for line in \
#            f:
#        for ch in line:
#            list.append(ch)
#length_list=len(list)
#index=0;

#print(list,type(list))
ser=serial.Serial('/dev/ttyUSB0',baudrate=115200,timeout=1)
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
def read_data_from_text():#text file is assumed to have the following format--Kp
#																			  Ki
#																			..Kd
#																			..set_point
	binary_list=[]
	length_list=0
	file1 = open("./system_values.txt", 'r')
	Lines_list = file1.readlines()
	for i in range(len(Lines_list)-1):
		Lines_list[i]=float(Lines_list[i][:-1])#'\n is a single character'
		binary_list.append(binary(Lines_list[i])[:-5])
	Lines_list[-1]=int(Lines_list[-1][:-1])
	binary_list.append('{0:09b}'.format(Lines_list[-1]))
	final_bytes_list=[]
	for i in range(len(binary_list)-1):
		k=2
		while k>=0:
			x=binary_list[i][8*k:(k+1)*8]
			final_bytes_list.append(x)
			k=k-1
	final_bytes_list.append(binary_list[-1][1:])
	final_bytes_list.append("0000000"+binary_list[-1][0])
	return final_bytes_list
def hack_for_ser_write(binary_string="10010001"):
	integer_val=int(binary_string,2)
	num_bytes=1
	bytes=integer_val.to_bytes(num_bytes,'big')
	return bytes
	
def hack_for_ser_read(string):#This guy will  give integer value, pass the ser.read() value directly
	string=str(string)
	if len(string)==3:
		return None
	elif len(string)==4:
		return int(ord(string[2]))
	elif len(string)>4:
		return int(string[4:6],16)
while 1:
# write your code here



ser.close()


