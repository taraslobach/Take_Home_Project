from __future__ import annotations

from src.ui.pages.forms_page import FormsPage
from src.ui.pages.main_page import MainPage
from src.ui.pages.wait_conditions_page import WaitConditionsPage
from utils.allure import allure_steps
from selene.support.shared import browser
import config


@allure_steps
class PlaygroundUiClient:
    # Pages
    main_page = MainPage()
    wait_conditions_page = WaitConditionsPage()
    forms_page = FormsPage()

    def open_login_page(self) -> PlaygroundUiClient:
        browser.driver.maximize_window()
        browser.open(config.playground_urls.main_page)
        return self


playground = PlaygroundUiClient()
