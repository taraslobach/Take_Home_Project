from __future__ import annotations

import os
import time

from data.constans import ErrorValidationMsg, FileCheck
from src.ui.playground import playground
from utils.allure import allure_steps


@allure_steps
class FormsActions:
    def verify_forms_with_validations(self) -> FormsActions:
        playground.forms_page.click_on_submit_form_btn()
        playground.forms_page.verify_city_error_msg(ErrorValidationMsg.CITY_VALIDATION)
        playground.forms_page.verify_state_error_msg(ErrorValidationMsg.STATE_VALIDATION)
        playground.forms_page.verify_zip_error_msg(ErrorValidationMsg.ZIP_VALIDATION)
        playground.forms_page.verify_agreement_error_msg(ErrorValidationMsg.AGREEMENT_VALIDATION)
        return self

    def verify_non_eng_locators(self) -> FormsActions:
        playground.forms_page.verify_non_eng_input('Something')
        playground.forms_page.verify_non_eng_checkbox()
        return self

    def verify_basic_form_controls(self) -> FormsActions:
        playground.forms_page.set_experience('5')
        playground.forms_page.mark_python_checkbox()
        playground.forms_page.choose_selenium_radio_btn()
        playground.forms_page.choose_selenium_from_dropdown()
        playground.forms_page.set_notes('QA Notes')
        playground.forms_page.verify_read_only_field()
        playground.forms_page.click_on_german_switcher()
        playground.forms_page.verify_switcher_enabled()
        playground.forms_page.set_fluency_level('4')
        playground.forms_page.verify_fluency_level('3')
        playground.forms_page.verify_disabled_textbox()
        return self

    def verify_file_is_downloaded(self) -> FormsActions:
        playground.forms_page.click_on_download_file()
        time.sleep(3)
        downloaded_file_path = os.path.join(os.path.expanduser('~'), FileCheck.FOLDER, FileCheck.FILE_NAME)
        assert os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        return self

    def upload_file(self) -> FormsActions:
        playground.forms_page.click_on_download_file()
        time.sleep(2)
        downloaded_file_path = os.path.join(os.path.expanduser('~'), FileCheck.FOLDER, FileCheck.FILE_NAME)
        playground.forms_page.fill_file_input(downloaded_file_path)
        playground.forms_page.verify_file_uploaded()
        os.remove(downloaded_file_path)
        return self

    def upload_multiply_files(self) -> FormsActions:
        playground.forms_page.download_multiple_files()
        time.sleep(2)
        downloaded_file_path = os.path.join(os.path.expanduser('~'), FileCheck.FOLDER, FileCheck.FILE_NAME)
        downloaded_file_path2 = os.path.join(os.path.expanduser('~'), FileCheck.FOLDER, FileCheck.ADDITIONAL_FILE)
        playground.forms_page.upload_multi_files(downloaded_file_path)
        playground.forms_page.upload_multi_files(downloaded_file_path2)
        playground.forms_page.verify_uploaded_files()
        os.remove(downloaded_file_path)
        os.remove(downloaded_file_path2)
        return self


forms_actions = FormsActions()
