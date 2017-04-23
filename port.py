import serial

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
def brate(baud):
    comp1_in.baudrate=baud
    comp2_in.baudrate=baud
    comp2_out.baudrate=baud
    comp3_in.baudrate=baud
    comp3_out.baudrate=baud
    comp1_out.baudrate=baud


pravila = {'1to2':[comp1_out,comp2_in],
           '1to3':[comp1_out,comp2_in,comp2_out,comp3_in],
           '2to1':[comp2_out,comp3_in,comp3_out,comp1_in],
           '2to3':[comp2_out,comp3_in],
           '3to1':[comp3_out,comp1_in],
           '3to2':[comp3_out,comp1_in,comp1_out,comp2_in]}



