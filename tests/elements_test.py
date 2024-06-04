import time

from pages.elements_page import TextBoxPage
from fixtures.conftest import driver


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_cur_add, output_per_add = text_box_page.check_filled_form()
            assert full_name == output_full_name, "Full name does not match"
            assert email == output_email, "Email does not match"
            assert current_address == output_cur_add, "Current address does not match"
            assert permanent_address == output_per_add, "Permanent address does not match"
            # input_data = text_box_page.fill_all_fields()
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data
            time.sleep(2)