from elements.profile_form_elements import ProfileFormSelectors
from pages.base_page import BasePage


class ProfileForm(BasePage):
    
    def __init__(self, driver, time_out = 10):
        super().__init__(driver=driver, time_out=time_out)
           
    def fill_in_name(self, name):
        return self.fill_input_field(ProfileFormSelectors.FIRST_NAME_ID, name)
    
    def fill_in_surname(self, surname):
        return self.fill_input_field(ProfileFormSelectors.SURNAME_ID, surname)
        
    def fill_in_email(self, email):
        return self.fill_input_field(ProfileFormSelectors.EMAIL_ID, email)
    
    def fill_in_mobile(self, mobile):
        return self.fill_input_field(ProfileFormSelectors.MOBILE_ID, mobile)
        
    def fill_in_country(self, country):
        return self.fill_input_field(ProfileFormSelectors.COUNTRY_ID, country)
    
    def fill_in_state(self, state):
        return self.fill_input_field(ProfileFormSelectors.STATE_ID, state)
    
    def fill_in_postcode(self, postcode):
        return self.fill_input_field(ProfileFormSelectors.POSTCODE_ID, postcode.replace(" ", ""))
    
    def select_gender_from_dropdown(self, gender):
        return self.select_dropdown_by_value(ProfileFormSelectors.GENDER_ID, gender)
    
    def select_marital_status(self, marital_status):
        return self.select_dropdown_by_value(ProfileFormSelectors.MARITAL_STATUS, marital_status)
    
    def select_id_type_from_dropdown(self, id_type):
        return self.select_dropdown_by_value(ProfileFormSelectors.ID_TYPE, id_type)
    
    def select_signature_from_dropdown(self, signature):
        return self.select_dropdown_by_value(ProfileFormSelectors.SIGNATURE_ID, signature)
    
    def click_profile_save_button(self):
        self.click_button(ProfileFormSelectors.BUTTON_ID)
       

   




