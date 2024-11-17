from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RegionMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    input_field = (By.TAG_NAME, "input")
    partners_list = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel__list-l')

    def select_region(self, region_name: str):
        """
        Выбрать регион из списка
        :param region_name: название региона
        :return: регион
        """

        region = (By.XPATH, f'//*[contains(text(),"{region_name}")]')
        self.find_element(region).click()