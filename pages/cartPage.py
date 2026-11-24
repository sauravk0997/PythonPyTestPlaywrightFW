from playwright.sync_api import Page, expect
from utilities.configReader import configReader
from pages.basePage import BasePage
from utilities.baseClass import BaseClass

class CartPage(BasePage, BaseClass):

    def __init__(self, page: Page):
        super().__init__(page)
        # self.page = page
        self.checkoutButton = self.get_dynamic_by_role("button", name="Checkout")
        self.continueShoppingButton = self.get_dynamic_by_locator("#continue-shopping")
        self.removeButton = self.get_dynamic_by_role("button", name="Remove")

    def click_checkout(self):
        self.click(self.checkoutButton)

    def click_continueShopping(self):
        self.click(self.continueShoppingButton)

    def click_remove(self):
        self.click(self.removeButton)

    def isOpened(self):
        cartPageURL = configReader.readConfig("Assert URL", "cartPageURL")
        self.verifyURL(cartPageURL)
