from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.CustomLogger as cl


class ContactForm(BasePage):
    def __int__(self, driver):
        super().__int__(driver)
        self.driver = driver

    # Locators values in contact us form
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pageTitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # test

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Clicked on contact us Form Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, "text")
        assert element == True
        cl.allureLogs("Contact Us Form Page Opened")

    def enterName(self):
        self.sendText("Sudeep", self._enterName, "text")
        cl.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("sudeepyadav5@gmail.com", self._enterEmail, "text")
        cl.allureLogs("Entered Email")

    def enterAddress(self):
        self.sendText("Surat", self._enterAddress, "text")
        cl.allureLogs("Entered Address")

    def enterMNumber(self):
        self.sendText("91-8460905553", self._enterMobileNumber, "index")
        cl.allureLogs("Entered Mobile Number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, "text")
        cl.allureLogs("Clicked on Submit Button")

