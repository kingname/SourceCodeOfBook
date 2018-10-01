from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver') #填写你的chromedriver的路径
driver.get("https://www.zhihu.com/#signin")

elem = driver.find_element_by_name("account") #寻找账号输入框
elem.clear()
elem.send_keys("xxx@gmail.com") #输入账号
password = driver.find_element_by_name('password') #寻找密码输入框
password.clear()
password.send_keys("12345678") #输入密码
input('请在网页上点击倒立的文字，完成以后回到这里按任意键继续。')
elem.send_keys(Keys.RETURN) #模拟键盘回车键
time.sleep(10) #这里可以直接sleep, 也可以使用上一章讲到的等待某个条件出现
print(driver.page_source)
driver.quit()
