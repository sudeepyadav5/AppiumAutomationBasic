import time
import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = ('C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

element_cont_desc = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Btn3")')
element_cont_desc.click()