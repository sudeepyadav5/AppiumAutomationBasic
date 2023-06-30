import time

import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = ('C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the button", element_id.text)
print("Text on the Button", element_id.get_attribute("text"))
print("Context description of the Button", element_id.get_attribute("content-desc"))
element_id.click()


time.sleep(2)

element_class = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
element_class.send_keys("Sudeep Yadav")
time.sleep(2)
element_class.clear()
time.sleep(2)
element_class.send_keys("Sudeep Yadav")

time.sleep(2)
driver.quit()

