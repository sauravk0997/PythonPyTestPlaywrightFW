from playwright.sync_api import Page
from pages.basePage import BasePage
from utilities.baseClass import BaseClass

class AboutPage(BasePage, BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.headingText = self.get_dynamic_by_text("Try Sauce AI FOR FREE")

    def isHeadingPresent(self):
        self.is_visible(self.headingText)

    def isOpened(self):
        pass