from tkinter.tix import Select
from unittest import TestCase, main

from time import sleep

from driver import get_driver
from elements.profile_form_elements import PageAttributes, ProfileFormSelectors
from pages.profile_page import ProfileForm


class VirtualBankDashboardTest(TestCase):
    @classmethod
    def setUpClass(cls):
        
        print("Beginning test setup, please wait...")   
        TIMEOUT     = 10
        cls.driver  = get_driver()
        cls._form   = ProfileForm(driver=cls.driver, time_out=TIMEOUT)
        cls._form.init()
     
    def setUp(self):
        """"""
        self.first_name     = "testName"
        self.surname        = "testSurname"
        self.email          = "test@example.com"
        self.mobile         = "07957199999"
        self.gender         = "male"
        self.marital_status = "single"
        self.country        = "United Kingdom"
        self.state          = "testState"
        self.postcode       = "testEU"
        self.id_type        = "national-id"
        self.signature      = "draw"
        
    def test_site_open(self):
        self.assertIn(PageAttributes.TITLE, self.driver.title)
    
    def test_profile_form(self):
        sleep(3)
        self._validate_profile_form(self._form.fill_in_name(self.first_name), self.first_name)
        self._validate_profile_form(self._form.fill_in_surname(self.surname), self.surname)
        self._validate_profile_form(self._form.fill_in_email(self.email), self.email)
        self._validate_profile_form(self._form.fill_in_mobile(self.mobile), self.mobile)
        self._validate_profile_form(self._form.fill_in_country(self.country), self.country)
        self._validate_profile_form(self._form.fill_in_state(self.state), self.state)
        self._validate_profile_form(self._form.fill_in_postcode(self.postcode), self.postcode)

        self._validate_select_value(self._form.select_gender_from_dropdown(self.gender), self.gender)
        self._validate_select_value(self._form.select_marital_status(self.marital_status), self.marital_status)
        self._validate_select_value(self._form.select_signature_from_dropdown(self.signature), self.signature)
        self._validate_select_value(self._form.select_id_type_from_dropdown(self.id_type), self.id_type)

        self._form.click_profile_save_button()
        
        input("Press Enter in terminal to close the window...")
        
    def _validate_profile_form(self, element, expected_value):
       
        actual_value = element.get_attribute("value")
        element_id   = element.get_attribute("id")
        
        # Mobile number is automatically reformatted (e.g., to +44...)
        # so we only check that it has a value, not exact match
        if element_id != ProfileFormSelectors.MOBILE_ID:
            self.assertEqual(actual_value, expected_value)
        else:
            self.assertTrue(actual_value)
    
    def _validate_select_value(self, select_element: Select, expected_value: str):
        selected_option_value = select_element.first_selected_option.get_attribute("value")
        self.assertEqual(selected_option_value, expected_value)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    main()