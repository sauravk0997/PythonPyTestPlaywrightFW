from playwright.sync_api import Page
from pages.basePage import BasePage
from utilities.baseClass import BaseClass

class LoginPage(BasePage, BaseClass):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = self.get_dynamic_by_role("textbox", name="Username")
        self.password = self.get_dynamic_by_role("textbox", name="Password")
        self.loginButton = self.get_dynamic_by_locator("#login-button")

    def login_to_home(self, username: str, password: str):
        try:
            self.fill(self.username, username)
            self.fill(self.password, password)
            self.click(self.loginButton)
        except Exception as e:
            print(f"Unable to login to home page: {e}")


    def isOpened(self):
        pass
