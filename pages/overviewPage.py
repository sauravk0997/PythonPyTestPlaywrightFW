from playwright.sync_api import Page, expect
from utilities.configReader import configReader
from pages.basePage import BasePage
from utilities.baseClass import BaseClass

class OverviewPage(BasePage, BaseClass):

    def __init__(self, page: Page):
        super().__init__(page)
        self.finishButton = self.get_dynamic_by_role("button", name="Finish")
        self.backHomeButton = self.get_dynamic_by_role("button", name="Back Home")

    def click_finish_button(self):
        self.click(self.finishButton)

    def click_back_home_button(self):
        self.click(self.backHomeButton)

    def isOpened(self):
        overviewPageURL = configReader.readConfig("Assert URL", "overviewPageURL")
        self.verifyURL(overviewPageURL)

    def completePageOpemed(self):
        completePageURL = configReader.readConfig("Assert URL", "completePageURL")
        self.verifyURL(completePageURL)
