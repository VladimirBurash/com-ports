import serial
import time

# import serial
# import io
# ser = serial.serial_for_url('loop://', timeout=1)
# sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
#
# sio.write('010101010101010')
# sio.flush() # it is buffering. required to get the data out *now*
# hello = sio.readline()
# print(type(hello))
# print(hello)

# configure the serial connections (the parameters differs on the device you are connecting to)
# ser = serial.Serial(
#     port='COM2',
#     baudrate=9600,
#     parity=serial.PARITY_ODD,
#     stopbits=serial.STOPBITS_TWO,
#     bytesize=serial.SEVENBITS
# )
# s = serial.Serial(
#     port='COM3',
#     baudrate=9600,
#     timeout=1
# )
# ser.isOpen()
# s.isOpen()
#
# ser.write(b'6783968761321758962478698')
#
# time.sleep(3)
#
#
# ser.close()
#
# s.inWaiting()
# # x = s.read()
# r = s.read(100000)
# out = int(r.decode('utf-8'))
# print(out)
#
# s.close()

comp1_in =serial.Serial(
    port='COM7',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
comp1_out = serial.Serial(
    port='COM2',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
comp2_in = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
comp2_out = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
comp3_in = serial.Serial(
    port='COM5',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
comp3_out = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

pravila = {'1to2':[comp1_out,comp2_in],
           '1to3':[comp1_out,comp2_in,comp2_out,comp3_in],
           '2to1':[comp2_out,comp3_in,comp3_out,comp1_in],
           '2to3':[comp2_out,comp3_in],
           '3to1':[comp3_out,comp1_in],
           '3to2':[comp3_out,comp1_in,comp1_out,comp2_in]}







