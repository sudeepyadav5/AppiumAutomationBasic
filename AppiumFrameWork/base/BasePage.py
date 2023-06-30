import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.CustomLogger as cl


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    log = cl.customLogger()

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorValue))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index("%d")' % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '$s' % locatorValue))
            return element
        else:
            self.log.info("Locator value" + locatorValue + "Not Found")
        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element Found with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Element Not Found with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)

        return element

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue)

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue + "is displayed")
            return True
        except:
            self.log.info("Element with Locator Type:" + locatorType + "and with Locator Value :" + locatorValue + "is not displayed")
            return False

    def screenshot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path :" + screenshotPath)
        except:
            self.log.info("Unable to save Screenshot to Path :" + screenshotPath)
