from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')

try:
    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
except Exception as _:
    print('网页加载太慢，不想等了。')

element = driver.find_element_by_xpath('//div[@class="content"]')
print(f'异步加载的内容是：{element.text}')

driver.quit()

# html = driver.page_source
# print(html)
# input('按任意键结束。')

# element = driver.find_element_by_id("passwd-id") #如果有多个符合条件的，返回第一个
# element = driver.find_element_by_name("passwd") #如果有多个符合条件的，返回第一个
# element_list = driver.find_elements_by_id("passwd-id") #以列表形式返回所有的符合条件的element
# element_list = driver.find_elements_by_name("passwd") #以列表形式返回所有的符合条件的element
# comment = driver.find_element_by_xpath('//div[@class="content"]')
# print(comment.text)
#
# comment = driver.find_elements_by_xpath('//p[starts-with(@id, "content_")]')
# for each in comment:
#     print(each.text)


