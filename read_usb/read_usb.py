#author sanoob aboo husain

import serial
import sys


def read_serial(port, baud_rate, mode):
    ser = serial.Serial(port, timeout=None,baudrate=baud_rate, xonxoff=False, rtscts=False, dsrdtr=False)
    count = 0;
    while True:
        if mode=='line':
            line = ser.readline()
            print line
        elif mode=='stream':
            line_ = ''
            while count < 60:
                line_ = line_+ser.read()
                count=count+1
            line_ = line_+ser.read()
            print line_
            count = 0
    ser.close()


try:
    port = sys.argv[1]
    baud = sys.argv[2]
    mode = sys.argv[3]
    read_serial(port, baud, mode)
    #read_serial('/dev/ttyUSB0', 9600, 'stream')
except Exception as exc:
    print '***************************************'
    print 'Usage: read_usb <PORT> <BAUD> <MODE>'
    print '     PORT - port id eg: /dev/ttyUSB0'
    print '     BAUDRATE - baud rate eg: 9600'
    print '     MODE - read mode line\stream '
    print '                 line-read line by line'
    print '                 stream-read stream'
    print '***************************************'
    print 'Error: '
    print exc
