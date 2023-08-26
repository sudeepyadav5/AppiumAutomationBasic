from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start(args=['--base-path', '/wd/hub'])

# Step 4 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Xiaomi M2006C3MII'
desired_caps['app'] = 'C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(MobileBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
driver.quit()

# Step 5 : Call stop method by using Appium Service class object
appium_service.stop()


"""from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

# Step 1: Import AppiumServiceBuilder class
from appium.webdriver.appium_service import AppiumService

# Step 2: Create an AppiumServiceBuilder object
appium_service = AppiumService()

try:
    # Step 3: Start the Appium server using the AppiumServiceBuilder object
    appium_service.start(args=['--base-path', '/wd/hub'])
    print("Appium Server Started Successfully.....")

    # Step 4: Create "Desired Capabilities"
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': '10',
        'deviceName': 'Xiaomi M2006C3MII',
        'app': 'C:/Users/3Embed/Python_Ast/ApkFile/Android_Demo_App.apk',
        'appPackage': 'com.code2lead.kwad',
        'appActivity': 'com.code2lead.kwad.MainActivity'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    ele_id = driver.find_element(MobileBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    print("##############-- Script Run Successfully--####################")

    time.sleep(5)
    driver.quit()

except Exception as e:
    print("An error occurred:", str(e))

finally:
    try:
        # Step 5: Stop the Appium server using the AppiumServiceBuilder object
        appium_service.stop()
        print(".....Appium Server Stopped Successfully")
    except Exception as e:
        print("An error occurred while stopping the server:", str(e))
"""
