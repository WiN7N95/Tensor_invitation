import os
import re
from pages.SbisHomePage import SbisHomePage
from pages.SbisDownloadPage import SbisDownloadPage

class TestCases:
     def test_case_03(self, driver):
        """Тест-кейс №3, дополнительный сценарий"""

        sbis_page = SbisHomePage(driver)
        sbis_dl = SbisDownloadPage(driver)

        file_name = "sbis_plugin.exe"
        dir_path = os.path.abspath(os.path.dirname(__file__))  # Подставляем путь до локальной директории
        file_path = os.path.join(dir_path, file_name)  # Добавляем к пути имя скачанного файла

        # Шаг 1
        sbis_page.open()

        # Шаг 2
        element = sbis_page.find_element(sbis_page.footer_dl, arrow_down=True)
        element.click()

        # Шаг 3
        sbis_dl.find_element(sbis_dl.tab_plugin).click()
        sbis_dl.find_element(sbis_dl.windows_tab).click()
        download_btn = sbis_dl.find_element(sbis_dl.download_btn)
        source = sbis_dl.get_url_link(download_btn)
        sbis_dl.save_file(file_path=file_path, source=source)

        # Шаг 4
        sbis_dl.check_file_saved(file_path)

        # Шаг 5
        file_size = re.findall(r'\d+\.\d+', download_btn.text)[0]
        sbis_dl.check_file_size(file_path=file_path, file_size=file_size)

        # Дополнительно удалить файл после прохождения теста
        os.remove(path=file_path)
