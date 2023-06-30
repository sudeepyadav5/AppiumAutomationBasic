import time

import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = ('C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])

# ele = wait.until(lambda x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ScrollView"))
# ele.click()

# ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'))
ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("LONG CLICK")'))

actions = TouchAction(driver)
actions.long_press(ele,5)
actions.perform()

# actions = ActionChains(driver)
# actions.click_and_hold(ele).perform()

time.sleep(4)
driver.quit()