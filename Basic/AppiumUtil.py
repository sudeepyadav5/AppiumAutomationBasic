from appium.webdriver.appium_service import AppiumService


class AppiumUtil:
    def __init__(self):
        self.appium_service = AppiumService()

    def connect(self):
        self.appium_service.start()