import time
import redis
import threading
from uiautomator import Device


class PhoneThread(threading.Thread):
    def __init__(self, serial):
        threading.Thread.__init__(self)
        self.serial = serial
        self.device = Device(serial)
        self.client = redis.StrictRedis()

    def run(self):
        while self.client.llen('game_name') != 0:
            game_name = self.client.lpop('game_name')
            if game_name:
                game_name = game_name.decode()
                self.crawl(game_name)

    def crawl(self, game_name):
        input_box = self.device(resourceId='com.taptap:id/input_box')
        input_box.clear_text()
        input_box.set_text(game_name)
        self.device(resourceId="com.taptap:id/search_btn").click()
        search_result = self.device(textContains=game_name, resourceId="com.taptap:id/app_title")
        if search_result.wait.exists(timeout=3000):
            search_result.click()
        else:
            self.crawl(game_name)
            return
        download_count = self.device(resourceId="com.taptap:id/download_count")
        if download_count.wait.exists(timeout=3000):
            print(game_name, download_count.text)
        self.device.press.back()


client = redis.StrictRedis()
with open('target', encoding='utf-8') as f:
    game_list = [x.strip() for x in f.readlines()]
with open('phone_list', encoding='utf-8') as f:
    serial_list = [x.strip() for x in f.readlines()]

for game in game_list:
    client.lpush('game_name', game)

phone_list = []
for serial in serial_list:
    phone_thread = PhoneThread(serial)
    phone_thread.start()
    phone_list.append(phone_thread)

while phone_list:
    phone_list = [x for x in phone_list if x.is_alive()]
    time.sleep(5)

