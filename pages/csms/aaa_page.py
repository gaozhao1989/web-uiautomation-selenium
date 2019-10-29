from selenium.webdriver.common.by import By
from pages import base_page


class AAAPage(base_page.BasePage):

    kw = (By.ID, 'kw')

    def is_page_persent(self):
        return self.is_displayed(self.kw)