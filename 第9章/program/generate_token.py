from selenium import webdriver
import time

service_args = ["--proxy=127.0.0.1:8080", '--ignore-ssl-errors=yes']


def run():
    print('start to Token')
    driver = webdriver.PhantomJS(service_args=service_args)
    driver.get('http://xxxx')
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    run()