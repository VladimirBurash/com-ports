import time

from open_con import open_connect
from send_data import send_data
from close_con import close_connect
from one_file import s

open_connect('1to3')
time.sleep(3)
send_data('1to3', b'1111111111111111')
close_connect('1to3')

time.sleep(5)