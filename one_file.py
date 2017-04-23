import serial,time
from port import comp1_in,comp1_out,comp2_in,comp2_out,comp3_in,comp3_out,pravila

get_connect = b'1111111111111111'

def s(to,data):

    computers = reversed(to.split('to'))
    reversed_way = '{}to{}'.format(*computers)

    res = get_connect

    for i,com in enumerate(pravila[to]):
        if i/2 == 1 or i == 0:
            com.isOpen()
            com.write(res)
            com.close()
        if i/2 != 1 and i != 0:
            com.isOpen()
            response = com.read(16)
            res = response
            com.close()
        print(com.port)


    for i,com in enumerate(pravila[reversed_way]):
        if i / 2 == 1 or i == 0:
            com.isOpen()
            com.write(res)
            com.close()
        if i / 2 != 1 and i != 0:
            com.isOpen()
            response = com.read(16)
            res = response
            com.close()

    if res == get_connect:
        print('Соединение открыто',res)
    time.sleep(5)

    res_data = b''
    rdata = data

    for i, com in enumerate(pravila[to]):

        if i / 2 == 1 or i == 0:
            com.isOpen()
            com.open()
            com.write(rdata)
            com.close()

        if i / 2 != 1 and i != 0:
            com.isOpen()
            com.open()
            print(com.in_waiting)
            s_data = com.read(16)
            res_data = s_data
            print(res_data, com.port)
            com.close()

    if res_data == data:
        print('Данные переданы:', res_data)
    time.sleep(5)
    computers = reversed(to.split('to'))
    reversed_way = '{}to{}'.format(*computers)

    res = get_connect

    for i, com in enumerate(pravila[to]):
        if i / 2 == 1 or i == 0:
            com.open()
            com.write(res)
            print('Пакет передан')
            com.close()
        if i / 2 != 1 and i != 0:
            com.open()
            response = com.read(16)
            res = response
            print(response, com.port)
            com.close()

    for i, com in enumerate(pravila[reversed_way]):
        if i / 2 == 1 or i == 0:
            com.open()
            com.write(res)
            com.close()
        if i / 2 != 1 and i != 0:
            com.open()
            response = com.read(16)
            res = response
            com.close()

    if res == get_connect:
        print('Соединение закрыто', res)