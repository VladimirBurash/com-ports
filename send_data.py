from port import comp1_in,comp1_out,comp2_in,comp2_out,comp3_in,comp3_out,pravila
import time
def send_data(to,data):
    res_data = b''
    rdata = data

    for i,com in enumerate(pravila[to]):

        if i/2 == 1 or i == 0:
            com.isOpen()
            com.write(rdata)

        if i/2 != 1 and i != 0:
            com.isOpen()
            print(com.in_waiting)
            s_data = com.read(16)
            res_data = s_data
            print(res_data,com.port)

        return res_data

