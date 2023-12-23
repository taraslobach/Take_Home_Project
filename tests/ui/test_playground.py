import allure
import pytest

from src.ui.actions.forms import forms_actions
from src.ui.actions.wait_conditions import wait_conditions_actions
from src.ui.playground import playground


@pytest.fixture(autouse=True)
def pre_test():
    playground.open_login_page()


@allure.title('Test wait conditions')
def test_wait_conditions():
    playground.main_page.navigate_to_wait_conditions_page()
    wait_conditions_actions.verify_accepted_alert() \
        .verify_accepted_prompt() \
        .verify_cancelled_prompt() \
        .verify_element_visibility() \
        .verify_element_invisibility() \
        .verify_element_enabled() \
        .verify_page_title_is_changed() \
        .verify_input_changed() \
        .verify_frame()


@allure.title('Test forms')
def test_forms():
    playground.main_page.navigate_to_forms_page()
    forms_actions.verify_basic_form_controls() \
        .verify_forms_with_validations() \
        .verify_non_eng_locators() \
        .verify_file_is_downloaded() \
        .upload_file() \
        .upload_multiply_files()
