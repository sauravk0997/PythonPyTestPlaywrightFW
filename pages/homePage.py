from playwright.sync_api import Page, expect
from utilities.configReader import configReader
from pages.basePage import BasePage
from utilities.baseClass import BaseClass


class HomePage(BasePage, BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_to_cart = self.get_dynamic_by_role("button", name="Add to cart")
        self.cartLogo = self.get_dynamic_by_locator(".shopping_cart_link")
        self.menuButton = self.get_dynamic_by_text("Open Menu")
        self.logoutButton = self.get_dynamic_by_role("button", name="Logout")
        self.aboutButton = self.get_dynamic_by_text("About")
        self.inventory = self.get_dynamic_by_locator(".inventory_item_name")

    def add_product_to_cart(self):
        try:
            # self.add_to_cart.first.click()
            self.click(self.add_to_cart.first)
            self.click(self.cartLogo)
        except Exception as e:
            print(f"Error occurred while adding product to cart: {e}")

    def clickMenuButton(self):
        self.click(self.menuButton)

    def clickAbout(self):
        self.click(self.aboutButton)

    def clickLogout(self):
        try:
            self.clickMenuButton()
            self.click(self.logoutButton)
        except Exception as e:
            print(f"Error occurred while clicking logout button: {e}")

    def isOpened(self):
        homePageURL = configReader.readConfig("Assert URL", "homePageURL")
        self.verifyURL(homePageURL)

    def get_all_inventories(self):
        return self.inventory

    def get_inventories_count(self):
        return self.get_all_inventories().count()
