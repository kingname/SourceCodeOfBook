import time
import random
import threading


class PhoneThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(random.randint(10, 500))


phone_list = []
for i in range(10):
    phone = PhoneThread()
    phone.start()
    phone_list.append(phone)

while True:
    for phone in phone_list:
        if phone.is_alive():
            break
    else:
        break
    time.sleep(60)



# phone = PhoneThread()
# phone.start()
# print(f'目前子线程实例是否还活着：{phone.is_alive()}')
# print('主线程等5秒')
# time.sleep(5)
# print(f'现在子线程实例是否还活着：{phone.is_alive()}')



