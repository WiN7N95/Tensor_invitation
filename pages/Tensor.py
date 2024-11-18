from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class TensorHomePage(BasePage):
    """Главная страница компании Тензор"""

    power_in_people = (By.XPATH, "//*[text()[contains(.,'Сила в людях')]]")
    more_link = (By.CSS_SELECTOR, '[href="/about"].tensor_ru-Index__link')
    working_images = (By.CSS_SELECTOR, '.tensor_ru-About__block3 .s-Grid-col img')

    def is_power_in_people_visible(self):
        return self.find_element(self.power_in_people).is_displayed()

    def click_more_link(self):
        self.find_element(self.more_link).click()

    def get_working_images_sizes(self):
        images = self.driver.find_elements(*self.working_images)
        return [(image.size['width'], image.size['height']) for image in images]
