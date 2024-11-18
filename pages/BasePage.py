from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import os

class BasePage:
    """Базовый класс для страниц"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10, arrow_down=False):
        """Найти элемент и проскролить до него вниз по странице"""
        element = WebDriverWait(self.driver, timeout=time).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        if arrow_down:
            element.send_keys(Keys.ARROW_DOWN)

        WebDriverWait(self.driver, timeout=time).until(EC.visibility_of(element))
        return element

    def switch_windows(self, window: int):
        """Переключиться на другое окно браузера"""
        self.driver.switch_to.window(self.driver.window_handles[window])

    def get_url_link(self, element):
        """Получить ссылку из элемента"""
        return element.get_attribute('href')

    def save_file(self, file_path, source):
        """Сохранить контент файла"""
        with open(file_path, mode="wb") as file:
            file.write(source)  # Пишем байтовый объект напрямую

    def get_file_size(self, file_path: str):
        """Получить размер файла"""
        return round((os.path.getsize(file_path) / 1024 / 1024), 2)
