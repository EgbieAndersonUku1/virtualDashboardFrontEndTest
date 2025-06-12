from time import sleep

from pages.base_page import BasePage
from elements.add_funds_elements import (
    WalletDashboardSelector,
    PinPopupSelector,
    FundMyAccountPopSelector,
)


class WalletDashboard(BasePage):
    def __init__(self, driver, time_out=10):
        super().__init__(driver=driver, time_out=time_out)
         
    def _add_pin(self, pin: str):
        pass
        
    def fund_bank_account(self, amount):
        self.click_button(WalletDashboardSelector.ADD_NEW_CARD_BUTTON_ID)
        
        # more to write here
    
    def fund_wallet(self, amount):
        self.click_button(WalletDashboardSelector.ADD_FUNDS_BUTTON_ID)
        
        # more to write here
        
    def transfer_funds(self):
        self.click_button(WalletDashboardSelector.TRANSFER_FUNDS_BUTTON_ID)
        # more to write here
        
    def remove_card(self):
        self.click_button(WalletDashboardSelector.REMOVE_BUTTON_ID)
        # more to write here
        
 
    
        element = self._wait.until(EC.visibility_of_element_located((By.ID, button_id)))
        element.click()
        
        sleep(2)
        
        if self._is_pin_added:
            self._add_pin(PinPopupSelector.PIN_NUMBER)