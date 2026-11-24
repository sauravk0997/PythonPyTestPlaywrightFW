import pytest
from playwright.sync_api import Page, Locator, expect

@pytest.mark.usefixtures("page")
class BaseClass:

    # ===============================
    # Dynamic Locators
    # ===============================

    def get_dynamic_by_role(self, role: str, name: str = None, **kwargs) -> Locator:
        return self.page.get_by_role(role, name=name, **kwargs)

    def get_dynamic_by_text(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_text(text, **kwargs)

    def get_dynamic_by_label(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_label(text, **kwargs)

    def get_dynamic_by_placeholde(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_placeholder(text, **kwargs)

    def get_dynamic_by_title(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_title(text, **kwargs)

    def get_dynamic_by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def get_dynamic_by_alt_text(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_alt_text(text, **kwargs)

    def get_dynamic_by_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    # -------------------------------
    # Basic Browser Actions
    # -------------------------------

    def click(self, locator: Locator):
        locator.click()

    def double_click(self, locator: Locator):
        locator.dblclick()

    def right_click(selfself, locator: Locator):
        locator.click(button="right")

    def fill(self, locator: Locator, value: str):
        locator.fill(value)

    def clear(self, locator: Locator):
        locator.fill("")

    def click_at_locator_coordinates(self, locator: Locator):
        box = locator.bounding_box()
        if box is None:
            raise Exception("Element does not have a bounding box")
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        self.page.mouse.click(x, y)

    def click_at_coordinates(self, x, y):
        self.page.mouse.click(x, y)

    def check(self, locator: Locator):
        locator.check()

    def uncheck(self, locator: Locator):
        locator.uncheck()

    def hover(self, locator: Locator):
        locator.hover()

    def press(self, locator: Locator, key: str):
        locator.press(key)

    def select_dropdown(self, locator: Locator, value: str):
        locator.select_option(value)


    # -------------------------------
    # Drag and Drop
    # -------------------------------

    def drag_and_drop(self, source: Locator, target: Locator):
        source.drag_to(target)

    # -------------------------------
    # Multiple Tabs / Windows
    # -------------------------------

    def handle_new_tab(self, locator: Locator):
        with self.page.expect_popup() as popup_info:
            locator.click()

        return popup_info.value

    # -------------------------------
    # Dialog Handling
    # -------------------------------

    def accept_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def dismiss_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    def accept_dialog_with_text(self, text: str):
        self.page.once("dialog", lambda dialog: dialog.accept(text))

    # -------------------------------
    # Assertions
    # -------------------------------

    def is_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    def is_enabled(self, locator: Locator):
        expect(locator).to_be_enabled()

    def is_checked(self, locator: Locator):
        expect(locator).to_be_checked()

    def verify_text(self, locator: Locator, expected_text: str):
        expect(locator).to_have_text(expected_text)

    # ===============================
    # Auto Wait Methods
    # ===============================

    def wait_for_locators(self, locator: Locator, state : str = "visible", timeout: int = 10000):
        locator.wait_for(state=state, timeout=timeout)

    def wait_for_page_load(self, state: str = "load", timeout: int = 30000):
        self.page.wait_for_load_state(state, timeout=timeout)

    def wait_for_url(self, expected_url: str, timeout: int = 30000):
        self.page.wait_for_url(expected_url, timeout=timeout)

    # ===============================
    # Browser Navigation Methods
    # ===============================

    def navigate_to(self, url: str, timeout: int = 30000, wait_until: str = "load"):
        return self.page.goto(url, timeout=timeout, wait_until=wait_until)

    def navigate_back(self, timeout: int = 30000, wait_until: str = "load"):
        return self.page.go_back(timeout=timeout, wait_until=wait_until)

    def navigate_forward(self, timeout: int = 30000, wait_until: str = "load"):
        return self.page.go_forward(timeout=timeout, wait_until=wait_until)

    def refresh_page(self, timeout: int = 30000, wait_until: str = "load"):
        return self.page.reload(timeout=timeout, wait_until=wait_until)

    def get_current_url(self):
        return self.page.url

