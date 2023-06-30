import time
import driver as driver
import pytest
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

time.sleep(5)

driver.start_activity("com.google.android.youtube", "com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")

time.sleep(5)

driver.start_activity("com.code2lead.kwad", "com.code2lead.kwad.MainActivity")
time.sleep(5)
driver.quit()
# desired_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValu")
# desired_id.click()
