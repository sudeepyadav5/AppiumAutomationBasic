import time

import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = ('C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

#list of Selenium Exceptions
#https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText"))
ele.send_keys("Sudeep Yadav")

time.sleep(4)
driver.quit()