import serial,time
from port import comp1_in,comp1_out,comp2_in,comp2_out,comp3_in,comp3_out,pravila
# Нужно сделать при логине первого пользователя
# TODO link, не забыть спиздеть на защите
link = b'1111111111111111'

def open_connect(to):

    computers = reversed(to.split('to'))
    reversed_way = '{}to{}'.format(*computers)

    res = b''

    for i,com in enumerate(pravila[to]):
        if i/2 == 1 or i == 0:
            com.isOpen()
            com.write(res)
        if i/2 != 1 and i != 0:
            com.isOpen()
            response = com.read(16)
            res = response
        print(com.port)


    for i,com in enumerate(pravila[reversed_way]):
        if i / 2 == 1 or i == 0:
            com.isOpen()
            com.write(res)
        if i / 2 != 1 and i != 0:
            com.isOpen()
            response = com.read(16)
            res = response

    if res == link:
        print('Соединение открыто',res)
        return True
    else:
        return False






