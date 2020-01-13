from machine import *
import time
import random
import ustruct as struct

uart = UART(1,9600,bits=8,parity=None,stop=1,rx=16,tx=17)
H_Length = 0
L_Length = 1
H_D1 = 2
L_D1 = 3
H_D2 = 4
L_D2 = 5
H_D3 = 6
L_D3 = 7
H_D4 = 8
L_D4 = 9
H_D5 = 10
L_D5 = 11
H_D6 = 12
L_D6 = 13
H_D13 = 26
L_D13 = 27
H_CS = 28
L_CS = 29
reset = Pin(27, mode=Pin.OUT)
set_active = Pin(14, mode=Pin.OUT)
set_active(0)
set_active(1)
reset(0)
time.sleep(5.5)
reset(1)
time.sleep(10)

def read():
    read_buffer = 0
    read_buffer = uart.read()
    if read_buffer is None:
        return None
    else:
        print(read_buffer)
    data = struct.unpack('!BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', read_buffer)

    return {
            'H_Length': data[H_Length+2],
            'L_Length': data[L_Length+2],
            'H_D1': data[H_D1+2],
            'L_D1': data[L_D1+2],
            'H_D2': data[H_D2+2],
            'L_D2': data[L_D2+2],
            'H_D3': data[H_D3+2],
            'L_D3': data[L_D3+2],
            'H_D4': data[H_D4+2],
            'L_D4': data[L_D4+2],
            'H_D5': data[H_D5+2],
            'L_D5': data[L_D5+2],
            'H_D6': data[H_D6+2],
            'L_D6': data[L_D6+2],
            'H_D13': data[H_D13+2],
            'L_D13': data[L_D13+2],
            'H_CS': data[H_CS+2],
            'L_CS': data[L_CS+2],
            }
count = 0
while(count < 10000):
    data = read()
    if data is not None:
        PM1_S = data['H_D1']*256+data['L_D1']
        PM2_5_S = data['H_D2']*256+data['L_D2']
        PM10_S = data['H_D3']*256+data['L_D3']
        PM1_E = data['H_D4']*256+data['L_D4']
        PM2_5_E = data['H_D5']*256+data['L_D5']
        PM10_E = data['H_D6']*256+data['L_D6']
        print((PM1_S, PM2_5_S, PM10_S))
        print((PM1_E, PM2_5_E, PM10_E))
    count+=1
    time.sleep(0.001)
