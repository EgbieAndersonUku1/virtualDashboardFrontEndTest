
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from elements.profile_form_elements import PageAttributes


class BasePage:
    
    def __init__(self, driver, time_out = 10):
        
        self._TIMEOUT = time_out
        self._driver  = driver
              
        if not self._driver:
            raise ValueError("The driver was not found")
    
    def init(self):
        self._wait  = WebDriverWait(self._driver, self._TIMEOUT)
        self._driver.get(PageAttributes.URL)
        self._driver.maximize_window()
    
    
    def fill_input_field(self, element_id, value):
        
        self._validate(element_id, value)
        
        element = self._wait.until(EC.visibility_of_element_located((By.ID, element_id)))
        
        self._raise_error_if_element_is_empty(element)
        element.clear() 
        element.send_keys(value)
     
        return element
  
    def click_button(self, button_id):
        self._validate(button_id, '')
        element = self._wait.until(EC.visibility_of_element_located((By.ID, button_id)))
        self._raise_error_if_element_is_empty(element)
        element.click()
    
    
    def select_dropdown_by_value(self, element_id, value):
        
        self._validate(element_id, value)
        
        select = Select(self._wait.until(EC.visibility_of_element_located((By.ID, element_id))))
        
        self._raise_error_if_element_is_empty(select)
        
        select.select_by_value(value)
        return select
        
    def _validate(self, element_id, value):
        if not isinstance(element_id, str):
            raise TypeError(f'The element id must be type string. Expected type string but got type: {type(element_id)}')
        
        if not isinstance(value, str):
            raise TypeError(f'The element id must be type string. Expected type string but got type: {type(value)}')
    
    def _raise_error_if_element_is_empty(self, element):
        if not element:
            raise ValueError("Expected an element but got an empty field")
  




