import time

import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def deviceDriver(deviceId, sysPort):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
    desired_caps['udid'] = deviceId
    desired_caps['systemPort'] = sysPort
    desired_caps['app'] = 'C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk'
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver


def enterText(driver):

    desired_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    desired_id.click()

    time.sleep(3)

    element_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    element_classname.send_keys("Sudeep")

    time.sleep(10)
    driver.quit()


def test_deviceTest():
    d1 = deviceDriver('DMNZQK6TOFHIZDJJ', 8200)
    d2 = deviceDriver('emulator-5554', 8201)

    enterText(d1)
    enterText(d2)
