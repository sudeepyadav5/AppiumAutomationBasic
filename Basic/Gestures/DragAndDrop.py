import time

import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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

# list of Selenium Exceptions
# https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# dragdropelement = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/drag")
dragdropelement = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
dragdropelement.click()

time.sleep(2)

ele_logo_from = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))

ele_logo_to = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))

action = TouchAction(driver)

action.long_press(ele_logo_from).move_to(ele_logo_to).release().perform()
time.sleep(2)

ele_button_from = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/btnDrag"))

ele_button_to = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout3"))

# action = TouchAction(driver)

action.long_press(ele_button_from).move_to(ele_button_to).release().perform()

time.sleep(4)
driver.quit()
