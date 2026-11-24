from pages.basePage import BasePage
from utilities.baseClass import BaseClass
from playwright.sync_api import Page


class InventoryPage(BasePage, BaseClass):

    def __init__(self, page: Page):
        super().__init__(page)
        self.inventoryDetails = self.get_dynamic_by_locator(".inventory_details_desc.large_size")
        self.inventory_addToCartButton = self.get_dynamic_by_role("button", "Add to cart")
        self.backToProductsButton = self.get_dynamic_by_locator("#back-to-products")

    def get_inventory_details_text(self):
        return self.inventoryDetails.inner_text()

    def click_Inventory_AddToCartButton(self):
        self.click(self.inventory_addToCartButton)

    def click_back_ToProductsButton(self):
        self.click(self.backToProductsButton)

    def isOpened(self):
        pass


