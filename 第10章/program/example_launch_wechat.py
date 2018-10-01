from uiautomator import Device

device = Device()
input_box = device(resourceId='com.taptap:id/input_box')
input_box.set_text('123')


# device.watcher('In_Detail_to_Search').when(text='我的世界 Minecraft').when(text='预约').press.back()

# input_box = device(resourceId='com.taptap:id/input_box')
# input_box.clear_text()
# input_box.set_text('汉家江湖')

# input_box = device(resourceId='com.taptap:id/input_box')
# if input_box.exists:
#     input_box.set_text('汉家江湖')
# else:
#     print('搜索框不存在')

# if device.screen == 'on':
#     print('当前手机屏幕为点亮状态')
#     device.press.power()
# elif device.screen == 'off':
#     print('当前手机屏幕为关闭状态')
#     device.press.power()

# device.wakeup()  # 点亮屏幕
# device.sleep()  # 关闭屏幕


# for i in range(20):
#     game_title_list = device(resourceId='com.taptap:id/bottom_app_name')

#     for title in game_title_list:
#         print(title.text)
#     device(scrollable=True).scroll.vert.forward()

# print(device.dump())

# device(packageName='com.android.systemui')
# device(className='android.widget.FrameLayout')
# device(resourceId="com.android.systemui:id/clock")
# device(index="3", resourceId="com.android.systemui:id/mobile_combo")

# device(text='微信').click()