from port import comp1_in,comp1_out,comp2_in,comp2_out,comp3_in,comp3_out,pravila
import time
# TODO: ack noack
#  Функция отправляющая ацк чисто по кайфу. Ты вызываешь после проверки пакета байтов на поломки. Если все норм то в bool передаешь тру. Дальше сам поймешь
def send_ack(to,bool):
    ack = b'101010101010101010'
    noack = b'4813974891749141789'
    ack_data = b''

    if bool:
        for i,com in enumerate(pravila[to]):

            if i/2 == 1 or i == 0:
                com.isOpen()
                com.write(ack)

            if i/2 != 1 and i != 0:
                com.isOpen()
                print(com.in_waiting)
                ack_data = com.read(16)
                print(ack_data,com.port)

            return ack_data

    else:
        for i, com in enumerate(pravila[to]):

            if i / 2 == 1 or i == 0:
                com.isOpen()
                com.write(noack)

            if i / 2 != 1 and i != 0:
                com.isOpen()
                print(com.in_waiting)
                ack_data = com.read(16)
                print(ack_data, com.port)

            return ack_data

