from playwright.sync_api import Page, expect
from utilities.configReader import configReader
from pages.basePage import BasePage
from utilities.baseClass import BaseClass
from utilities.random_data import randomData

class InfoPage(BasePage, BaseClass):

    def __init__(self, page: Page):
        super().__init__(page)
        self.firstName = self.get_dynamic_by_role("textbox", name="First Name")
        self.lastName = self.get_dynamic_by_role("textbox", name="Last Name")
        self.zipCode = self.get_dynamic_by_role("textbox", name="Zip/Postal Code")
        self.continueButton = self.get_dynamic_by_locator("#continue")
        self.cancelButton = self.get_dynamic_by_role("button", name="cancel")

    def isOpened(self):
        infoPageURL = configReader.readConfig("Assert URL", "infoPageURL")
        self.verifyURL(infoPageURL)

    def fillForm(self):
        random_data = randomData()
        firstName = random_data.firstName()
        lastName = random_data.lastName()
        zipCode = random_data.zip_code()
        self.fill(self.firstName, firstName)
        self.fill(self.lastName, lastName)
        self.fill(self.zipCode, zipCode)

    def clickCancelButton(self):
        self.click(self.cancelButton)

    def click_continue_button(self):
        self.click(self.continueButton)
