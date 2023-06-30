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

# element_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text= "ENTER SOME VALUE"]')
# element_xpath.click()
#
# time.sleep(3)
desired_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
desired_id.click()

time.sleep(3)

element_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
element_classname.send_keys("Sudeep")

time.sleep(2)

# element_xpath_text = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="SUBMIT"]')
# element_xpath_text.click()

# element_xpath_class = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@id = "com.code2lead.kwad:id/Btn1"]')
# element_xpath_class.click()

# element_xpath_index = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@index[2]]')
# element_xpath_index.click()

element_xpath_res_id = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn1"]')
element_xpath_res_id.click()