import pytest

from pages.aboutPage import AboutPage
from pages.inventoryPage import InventoryPage
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.cartPage import CartPage
from pages.infoPage import InfoPage
from pages.overviewPage import OverviewPage
from utilities.baseClass import BaseClass
from utilities.excelData import ExcelUtilities
from utilities.PathUtilites import PathUtilities
from utilities.logger import generateLog
from utilities.loginDataUtilities import LoginDataUtilities


class TestE2EScenario1(BaseClass):

    @pytest.fixture(autouse=True)
    def _setup(self, page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.cart_page = CartPage(page)
        self.info_page = InfoPage(page)
        self.overview_page = OverviewPage(page)
        self.inventory_page = InventoryPage(page)
        self.about_page = AboutPage(page)
        self.excel_utilities = ExcelUtilities()

    @pytest.mark.regression
    @pytest.mark.parametrize("username, password", LoginDataUtilities.get_user("standard_user"))
    def test_E2EScenario(self, page, username, password):
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        self.home_page.add_product_to_cart()
        self.cart_page.isOpened()
        self.cart_page.click_checkout()
        self.info_page.isOpened()
        self.info_page.fillForm()
        self.info_page.click_continue_button()
        self.overview_page.isOpened()
        self.overview_page.click_finish_button()
        self.overview_page.completePageOpemed()
        self.overview_page.click_back_home_button()
        self.home_page.isOpened()
        self.home_page.clickLogout()

    @pytest.mark.parametrize("username, password", LoginDataUtilities.get_user())
    def test_login_all_data(self, page, username, password):
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        self.home_page.clickLogout()


    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password", LoginDataUtilities.get_user("standard_user"))
    def test_login_specific_user(self, page, username, password):
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        self.home_page.clickLogout()

    def test_login_excel_data(self, page):
        CONFIG_PATH = PathUtilities.get_test_data_path("user_data.xlsx")
        username = self.excel_utilities.get_cell_data(CONFIG_PATH, "Sheet2", 1, 2)
        password = self.excel_utilities.get_cell_data(CONFIG_PATH, "Sheet2", 2, 2)
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        self.home_page.clickLogout()

    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password", LoginDataUtilities.get_user("standard_user"))
    def test_aboutPage(self, page, username, password):
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        self.home_page.clickMenuButton()
        self.home_page.clickAbout()
        self.about_page.isHeadingPresent()
        self.about_page.navigate_back()
        self.home_page.isOpened()
        self.home_page.clickLogout()

    @pytest.mark.parametrize("username, password", LoginDataUtilities.get_user("standard_user"))
    def test_productDescripiton(self, page, username, password):
        self.login_page.login_to_home(username, password)
        self.home_page.isOpened()
        try:
            for inventory in range(self.home_page.get_inventories_count()):
                    self.home_page.get_all_inventories().nth(inventory).click()
                    logger = generateLog().log()
                    logger.info(self.inventory_page.get_inventory_details_text())
                    print(self.inventory_page.get_inventory_details_text())
                    self.inventory_page.click_Inventory_AddToCartButton()
                    self.inventory_page.click_back_ToProductsButton()
        except:
            print("Error occured while navigating to inventory page")
        self.home_page.clickLogout()








