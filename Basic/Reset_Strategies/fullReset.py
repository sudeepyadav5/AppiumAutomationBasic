import driver as driver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = 'C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['fullReset'] = True


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")\
# ele_id.click()

desired_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
desired_id.click()
