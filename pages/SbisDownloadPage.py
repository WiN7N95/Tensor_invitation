from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class SbisDownloadPage(BasePage):
    tab_plugin = (By.XPATH, "//div[text()[contains(.,'СБИС Плагин')]]")
    windows_tab = (By.XPATH, "//span[text()[contains(.,'Windows')]]")
    download_btn = (By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

    def click_plugin_tab(self):
        self.find_element(self.tab_plugin).click()

    def click_windows_tab(self):
        self.find_element(self.windows_tab).click()

    def get_download_button(self):
        return self.find_element(self.download_btn)
