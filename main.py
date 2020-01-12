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

def read():
    while True:
        set_active(1)
        reset(0)
        time.sleep(5.5)
        reset(1)
        time.sleep(5.5)
        #checksum = 0x42+0x4D+0xE4+0x00+0x00
        #serCmd = struct.pack('!BBBBBH',0x42,0x4D,0xE4,0x00,0x00,checksum)
        firstByte = uart.read(1)
        print(firstByte)
        secondByte = uart.read(1)
        print(secondByte)
        read_buffer = 0
        read_buffer = uart.read(30)
        print(read_buffer)
        data = struct.unpack('!BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', read_buffer)

        return {
                'H_Length': data[H_Length],
                'L_Length': data[L_Length],
                'H_D1': data[H_D1],
                'L_D1': data[L_D1],
                'H_D2': data[H_D2],
                'L_D2': data[L_D2],
                'H_D3': data[H_D3],
                'L_D3': data[L_D3],
                'H_D4': data[H_D4],
                'L_D4': data[L_D4],
                'H_D5': data[H_D5],
                'L_D5': data[L_D5],
                'H_D6': data[H_D6],
                'L_D6': data[L_D6],
                'H_D13': data[H_D13],
                'L_D13': data[L_D13],
                'H_CS': data[H_CS],
                'L_CS': data[L_CS],
                }
count = 0
while(count < 3):
    data = read()
    print(data)
