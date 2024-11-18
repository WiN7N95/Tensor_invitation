from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class RegionMenu(BasePage):
    input_field = (By.TAG_NAME, "input")
    
    def select_region(self, region_name: str):
        region = (By.XPATH, f'//*[contains(text(),"{region_name}")]')
        self.find_element(region).click()
