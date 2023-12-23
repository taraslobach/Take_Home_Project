from __future__ import annotations


from selene import be, have, browser
from selene.support.shared.jquery_style import s
from utils.allure import allure_steps


@allure_steps
class WaitConditionsPage:
    show_alert_btn = s('#alert_trigger')
    show_prompt_btn = s('#prompt_trigger')
    alert_handled = s('#alert_handled')
    success_prompt = s('#confirm_ok')
    cancelled_prompt = s('#confirm_cancelled')

    visibility_trigger_btn = s('#visibility_trigger')
    click_me_btn = s('#visibility_target')

    invisibility_trigger_btn = s('#invisibility_trigger')
    spinner_is_gone = s('#spinner_gone')

    enabled_trigger_btn = s('#enabled_trigger')
    enabled_target_btn = s('#enabled_target')

    page_title_trigger_btn = s('#page_title_trigger')

    text_value_trigger_btn = s('#text_value_trigger')
    input_field = s('#wait_for_value')
    confirm_btn = s('#wait_for_text')

    wait_for_frame_trigger_btn = s('#wait_for_frame')
    frame = s("//iframe[@id='frm']")
    inner_btn = s('#inner_button')

    def click_on_show_alert_btn(self):
        self.show_alert_btn.click()
        return self

    def click_on_show_prompt_btn(self):
        self.show_prompt_btn.click()
        return self

    def verify_alert_handled(self):
        self.alert_handled.should(be.visible)
        return self

    def verify_success_prompt(self):
        self.success_prompt.should(be.visible)
        return self

    def verify_cancelled_promt(self):
        self.cancelled_prompt.should(be.visible)
        return self

    def click_on_visibility_trigger_btn(self):
        self.visibility_trigger_btn.click()
        return self

    def verify_clickable_btn_appear(self):
        self.click_me_btn.should(be.visible).should(be.clickable)
        return self

    def click_on_invisibility_trigger_btn(self):
        self.invisibility_trigger_btn.click()
        return self

    def verify_spinner_is_gone(self):
        self.spinner_is_gone.should(have.exact_text('Thank God that spinner is gone!'))
        return self

    def click_on_enabled_trigger_btn(self):
        self.enabled_trigger_btn.click()
        return self

    def verify_btn_enabled(self):
        self.enabled_target_btn.should(have.css_property("btn btn-success"))
        return self

    def click_on_page_title_trigger_btn(self):
        self.page_title_trigger_btn.click()
        return self

    def click_on_text_value_trigger_btn(self):
        self.text_value_trigger_btn.click()
        return self

    def verify_field_are_filled(self):
        self.input_field.wait_until(be.visible)
        self.input_field.should(be.not_.blank)
        return self

    def verify_btn_text_changed(self):
        self.confirm_btn.should(have.text('Submit'))
        return self

    def click_on_wait_for_frame_trigger_btn(self):
        self.wait_for_frame_trigger_btn.click()
        return self

    def verify_frame_is_displayed(self):
        self.frame.wait_until(be.visible)
        self.frame.should(be.visible)
        return self

    def click_on_inner_btn(self):
        browser.driver.switch_to.frame('frm')
        self.inner_btn.click()
        return self

    def verify_inner_btn_changed(self):
        self.inner_btn.should(have.exact_text('Clicked'))
        return self
