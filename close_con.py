from port import comp1_in,comp1_out,comp2_in,comp2_out,comp3_in,comp3_out,pravila
# TODO UNLINK сделать
unlink = b'0000000000000000'

def close_connect(to):

    computers = reversed(to.split('to'))
    reversed_way = '{}to{}'.format(*computers)

    res = unlink

    for i,com in enumerate(pravila[to]):
        if i/2 == 1 or i == 0:
            com.write(res)
            com.close()

            print('Пакет передан')
        if i/2 != 1 and i != 0:
            response = com.read(16)
            res = response
            com.close()
            print(response,com.port)


    for i,com in enumerate(pravila[reversed_way]):
        if i / 2 == 1 or i == 0:
            com.write(res)
            com.close()
        if i / 2 != 1 and i != 0:
            response = com.read(16)
            res = response
            com.close()

    if res == unlink:
        print('Соединение закрыто',res)
        return True
    else:
        return False




