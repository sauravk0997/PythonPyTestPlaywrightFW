from abc import ABC, abstractmethod
from playwright.sync_api import Page, expect

class BasePage(ABC):

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def isOpened(self):
        pass

    def verifyURL(self, expected_url):
        self.page.wait_for_url(expected_url)
        expect(self.page).to_have_url(expected_url)