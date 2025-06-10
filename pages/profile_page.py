from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from elements.profile_form_elements import PageAttributes, ProfileFormSelectors


class ProfileForm:
    
    def __init__(self, driver, time_out = 10):
        
        self._TIMEOUT = time_out
        self._driver  = driver
              
        if not self._driver:
            raise ValueError("The driver was not found")
    
    def init(self):
        self._wait  = WebDriverWait(self._driver, self._TIMEOUT)
        self._driver.get(PageAttributes.URL)
        self._driver.maximize_window()
    
    def fill_in_name(self, name):
        return self._fill_input_field(ProfileFormSelectors.FIRST_NAME_ID, name)
    
    def fill_in_surname(self, surname):
        return self._fill_input_field(ProfileFormSelectors.SURNAME_ID, surname)
        
    def fill_in_email(self, email):
        return self._fill_input_field(ProfileFormSelectors.EMAIL_ID, email)
    
    def fill_in_mobile(self, mobile):
        return self._fill_input_field(ProfileFormSelectors.MOBILE_ID, mobile)
        
    def fill_in_country(self, country):
        return self._fill_input_field(ProfileFormSelectors.COUNTRY_ID, country)
    
    def fill_in_state(self, state):
        return self._fill_input_field(ProfileFormSelectors.STATE_ID, state)
    
    def fill_in_postcode(self, postcode):
        return self._fill_input_field(ProfileFormSelectors.POSTCODE_ID, postcode.replace(" ", ""))
    
    def select_gender_from_dropdown(self, gender):
        return self._select_dropdown_by_value(ProfileFormSelectors.GENDER_ID, gender)
    
    def select_marital_status(self, marital_status):
        return self._select_dropdown_by_value(ProfileFormSelectors.MARITAL_STATUS, marital_status)
    
    def select_id_type_from_dropdown(self, id_type):
        return  self._select_dropdown_by_value(ProfileFormSelectors.ID_TYPE, id_type)
    
    def select_signature_from_dropdown(self, signature):
        return  self._select_dropdown_by_value(ProfileFormSelectors.SIGNATURE_ID, signature)
    
    def _fill_input_field(self, element_id, value):
        
        self._validate(element_id, value)
        
        element = self._wait.until(EC.visibility_of_element_located((By.ID, element_id)))
        element.clear() 
        element.send_keys(value)
     
        return element
    
    def click_save_button(self):
        element = self._wait.until(EC.visibility_of_element_located((By.ID, ProfileFormSelectors.BUTTON_ID)))
        element.click()

    def _select_dropdown_by_value(self, element_id, value):
        
        self._validate(element_id, value)
        
        select = Select(self._wait.until(EC.visibility_of_element_located((By.ID, element_id))))
        select.select_by_value(value)
        return select
    
    def _validate(self, element_id, value):
        if not isinstance(element_id, str):
            raise TypeError(f'The element id must be type string. Expected type string but got type: {type(element_id)}')
        
        if not isinstance(value, str):
            raise TypeError(f'The element id must be type string. Expected type string but got type: {type(value)}')
  




