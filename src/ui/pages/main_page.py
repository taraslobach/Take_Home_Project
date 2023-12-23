from __future__ import annotations

from selene.support.shared.jquery_style import s, ss
from utils.allure import allure_steps


@allure_steps
class MainPage:
    available_pages = ss('.card')
    view_page_btn = s('//a[@class="btn btn-success"]')
    wait_conditions = s("a[href='expected_conditions.html']")
    keyboard_actions = s("a[href='keyboard_events.html']")
    mouse_actions = s("a[href='mouse_events.html']")
    popup_window = s("a[href='multi_window.html']")
    frames = s("a[href='frames.html']")
    forms = s("a[href='forms.html']")
    sample_pages = s("a[href='login.html']")
    advanced_ui_features = s("a[href='advanced.html']")

    def navigate_to_wait_conditions_page(self) -> MainPage:
        self.wait_conditions.click()
        return self

    def navigate_to_forms_page(self) -> MainPage:
        self.forms.click()
        return self

