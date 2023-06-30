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

Element_Class_Method = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

for x in Element_Class_Method:
    print(x.text)
    button = x.text
    if button == "ScrollView":
        x.click()
        break
time.sleep(2)
driver.quit()

