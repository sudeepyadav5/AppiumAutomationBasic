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

print("Is Displayed : ",element_id.is_displayed())
print("Is Enabled : ",element_id.is_enabled())
print("Is selected : ",element_id.is_selected())
print("Size : ",element_id.size)
print("Location : ",element_id.location)