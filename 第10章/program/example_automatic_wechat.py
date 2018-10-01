#! /Users/kingname/Project/scrapy_venv/bin/python

from uiautomator import Device

device = Device()
device.wakeup()

wechat_icon = device(text='微信')
if not wechat_icon.exists:
    device.swipe(400, 600, 0, 600)
if wechat_icon.exists:
    wechat_icon.click()

device(scrollable=True).scroll.vert.toBeginning()
while True:
    girl_friend = device(text='女朋友')
    if girl_friend.exists:
        girl_friend.click()
        break
    else:
        device(scrollable=True).scroll.vert.forward()

device(className="android.widget.EditText").set_text('早上好，本消息为自动发送。')
device.press.back()
send_button = device(text="发送")
if send_button.exists:
    send_button.click()
