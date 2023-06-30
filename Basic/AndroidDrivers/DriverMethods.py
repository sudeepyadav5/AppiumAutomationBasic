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


print("Check if device is Locked: ", driver.is_locked())
print("Current Package", driver.current_package)
print("Current Activity", driver.current_activity)
print("Current context", driver.current_context)
print("Current Orientation", driver.orientation)

# desired_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
# desired_id.click()
#
# time.sleep(3)
#
# element_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
# element_classname.send_keys("Sudeep")
