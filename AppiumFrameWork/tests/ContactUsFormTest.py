from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm
import AppiumFrameWork.utilities.CustomLogger as cl
import unittest
import pytest


# driver1 = Driver()
# log = cl.customLogger()
#
# driver = driver1.getDriverMethod()
#
# cf = ContactForm(driver)


# log.info("Launch Application")
# bp.screenshot("App")
# element = bp.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
# print(element)
# bp.clickElement("com.code2lead.kwad:id/ContactUs", "id")
# bp.sendText("Sudeep Yadav", "Enter Name", "text")
# bp.screenshot("code2lead")
@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("Application Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()

