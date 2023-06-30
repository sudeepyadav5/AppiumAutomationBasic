import AppiumFrameWork.utilities.CustomLogger as cl
import unittest
import pytest

from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.LoginPage import LoginPageTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.gt = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=3)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()

    @pytest.mark.run(order=2)
    def test_openLoginScreen(self):
        self.bp.keycode(4)
        #cl.allureLogs("Application Opened")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginButton()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order=1)
    def test_loginFailMethod(self):
        cl.allureLogs("Application Opened")
        self.gt.clickLoginButton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLoginButton()
        self.gt.verifyAdminScreen()




