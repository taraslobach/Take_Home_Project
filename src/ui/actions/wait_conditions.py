from __future__ import annotations

from selenium.webdriver.support.wait import WebDriverWait

from src.ui.playground import playground
from utils.allure import allure_steps
from selene import browser
from selenium.webdriver.support import expected_conditions


@allure_steps
class WaitConditionsActions:
    def verify_accepted_alert(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_show_alert_btn()
        WebDriverWait(browser.driver, 10).until(expected_conditions.alert_is_present())
        alert = browser.switch_to.alert
        assert alert.text == "I am alerting you!"
        alert.accept()
        playground.wait_conditions_page.verify_alert_handled()
        return self

    def verify_accepted_prompt(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_show_prompt_btn()
        WebDriverWait(browser.driver, 10).until(expected_conditions.alert_is_present())
        prompt = browser.switch_to.alert
        assert "Choose wisely...\nIt's your life!" == prompt.text
        prompt.accept()
        playground.wait_conditions_page.verify_success_prompt()
        return self

    def verify_cancelled_prompt(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_show_prompt_btn()
        WebDriverWait(browser.driver, 10).until(expected_conditions.alert_is_present())
        prompt = browser.switch_to.alert
        prompt.dismiss()
        playground.wait_conditions_page.verify_cancelled_promt()
        return self

    def verify_element_visibility(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_visibility_trigger_btn()
        playground.wait_conditions_page.verify_clickable_btn_appear()
        return self

    def verify_element_invisibility(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_invisibility_trigger_btn()
        playground.wait_conditions_page.verify_spinner_is_gone()
        return self

    def verify_element_enabled(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_enabled_trigger_btn()
        playground.wait_conditions_page.verify_btn_enabled()
        return self

    def verify_page_title_is_changed(self) -> WaitConditionsActions:
        start_title = browser.driver.title
        playground.wait_conditions_page.click_on_page_title_trigger_btn()
        WebDriverWait(browser.driver, 10).until_not(expected_conditions.title_contains(start_title))
        return self

    def verify_input_changed(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_text_value_trigger_btn()
        playground.wait_conditions_page.verify_field_are_filled()
        playground.wait_conditions_page.verify_btn_text_changed()
        return self

    def verify_frame(self) -> WaitConditionsActions:
        playground.wait_conditions_page.click_on_wait_for_frame_trigger_btn()
        playground.wait_conditions_page.verify_frame_is_displayed()
        playground.wait_conditions_page.click_on_inner_btn()
        playground.wait_conditions_page.verify_inner_btn_changed()
        return self


wait_conditions_actions = WaitConditionsActions()
