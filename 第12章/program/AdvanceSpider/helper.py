import time
import json
import redis
from selenium import webdriver

client = redis.StrictRedis()

driver = webdriver.Chrome('./chromedriver')
driver.get('http://exercise.kingname.info/exercise_login_success')
user = driver.find_element_by_xpath('//input[@name="username"]')
user.clear()
user.send_keys('kingname')

password = driver.find_element_by_xpath('//input[@name="password"]')
password.clear()
password.send_keys('genius')

remember = driver.find_element_by_xpath('//input[@name="rememberme"]')
remember.click()

login = driver.find_element_by_xpath('//button[@class="login"]')
login.click()
time.sleep(2)
cookies = driver.get_cookies()
client.lpush('cookies', json.dumps(cookies))
driver.quit()
