from __future__ import annotations

from selene import be, have
from selene.support.shared.jquery_style import s, ss
from utils.allure import allure_steps


@allure_steps
class FormsPage:
    experience = s('#exp')
    python_checkbox = s('#check_python')
    selenium_radio_btn = s("label[for='rad_selenium']")
    primary_skills_dropdown = s("//select[@id='select_tool']")
    dropdown_list = ss('#select_tool')
    choose_language = s("option[value='python']")
    notes = s('#notes')
    mandatory_skill = s('#common_sense')
    speaks_german_switcher = s("label[for='german']")
    switcher_status = s('#german_validate')
    german_fluency_slider = s('#fluency')
    german_fluency_value = s('#fluency_validate')
    upload_single_file = s('#upload_cv')
    upload_multiple_files = s('#upload_files')
    download_file = s('#download_file')
    validate_cv = s('#validate_cv')
    validate_files = s('#validate_files')
    current_salary = s('#salary')

    city = s('#validationCustom03')
    state = s('#validationCustom04')
    zip = s('#validationCustom05')
    agreement_checkbox = s("label[for='invalidCheck']")
    submit_form_btn = s("button[type='submit']")
    city_error_msg = s('#invalid_city')
    state_error_msg = s('#invalid_state')
    zip_error_msg = s('#invalid_zip')
    agreement_error_msg =s('#invalid_terms')

    non_eng_input = s('#नाव')
    non_eng_checkbox = s('#ગુજરાતી')

    def set_experience(self, years):
        self.experience.set(years)
        return self

    def mark_python_checkbox(self):
        self.python_checkbox.click()
        return self

    def choose_selenium_radio_btn(self):
        self.selenium_radio_btn.click()
        return self

    def choose_selenium_from_dropdown(self):
        self.primary_skills_dropdown.click()
        self.dropdown_list.element_by(have.value("sel")).click()
        return self

    def set_notes(self, note):
        self.notes.set(note)
        return self

    def verify_read_only_field(self):
        self.mandatory_skill.should(have.css_property('readonly'))
        return self

    def click_on_german_switcher(self):
        self.speaks_german_switcher.click()
        return self

    def verify_switcher_enabled(self):
        self.switcher_status.should(be.enabled)
        return self

    def set_fluency_level(self, level):
        self.german_fluency_slider.set_value(level)
        return self

    def verify_fluency_level(self, expected_level):
        self.german_fluency_value.should(have.exact_text(expected_level))
        return self

    def click_on_download_file(self):
        self.download_file.click()
        return self

    def download_multiple_files(self):
        self.download_file.double_click()
        return self

    def verify_disabled_textbox(self):
        self.current_salary.should(be.disabled)
        return self

    def set_city(self, city_name):
        self.city.set(city_name)
        return self

    def set_state(self, state_name):
        self.state.set(state_name)
        return self

    def set_zip(self, zip_code):
        self.zip.set(zip_code)

    def click_on_agreement_checkbox(self):
        self.agreement_checkbox.click()
        return self

    def click_on_submit_form_btn(self):
        self.submit_form_btn.click()
        return self

    def verify_non_eng_input(self, value):
        self.non_eng_input.set(value)
        return self

    def verify_non_eng_checkbox(self):
        self.non_eng_checkbox.click()
        return self

    def verify_city_error_msg(self, invalid_city_msg):
        self.city_error_msg.should(have.exact_text(invalid_city_msg))
        return self

    def verify_state_error_msg(self, invalid_state_msg):
        self.state_error_msg.should(have.exact_text(invalid_state_msg))
        return self

    def verify_zip_error_msg(self, invalid_zip_msg):
        self.zip_error_msg.should(have.exact_text(invalid_zip_msg))
        return self

    def verify_agreement_error_msg(self, agreement_error_msg):
        self.agreement_error_msg.should(have.exact_text(agreement_error_msg))
        return self

    def fill_file_input(self, value_path):
        self.upload_single_file.send_keys(value_path)
        return self

    def verify_file_uploaded(self):
        self.validate_cv.should(be.visible)
        return self

    def upload_multi_files(self, path):
        self.upload_multiple_files.send_keys(path)
        return self

    def verify_uploaded_files(self):
        self.validate_files.should(be.visible)
        return self
