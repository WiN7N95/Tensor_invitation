from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class SbisHomePage(BasePage):
    """Главная страница СБИС"""

    link = "https://sbis.ru/"
    contacts = (By.LINK_TEXT, "Контакты")
    tensor_link = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    partners_list = (By.CSS_SELECTOR, '[data-qa="list"]')
    footer_dl = (By.CSS_SELECTOR, '[href="/download"]')

    def open(self):
        """Открыть главную страницу"""
        self.driver.get(self.link)

    def click_contacts(self):
        self.find_element(self.contacts).click()

    def click_tensor_link(self):
        self.find_element(self.tensor_link).click()

    def click_region(self):
        self.find_element(self.region).click()

    def click_footer_download(self):
        self.find_element(self.footer_dl).click()

    def get_region_text(self):
        return self.find_element(self.region).text

    def get_partners_text(self):
        return self.find_element(self.partners_list).text
