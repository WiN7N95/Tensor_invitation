import os
import requests
from pages.SbisHomePage import SbisHomePage  # Импортируйте ваши страницы
from pages.SbisDownloadPage import SbisDownloadPage


class TestCases:

    def test_case_03(self, driver):
        sbis_page = SbisHomePage(driver)
        sbis_dl = SbisDownloadPage(driver)

        # Определяем имя файла и путь для сохранения
        file_name = "sbis_plugin.exe"
        file_path = os.path.join(os.path.dirname(__file__), file_name)

        # Выполняем шаги теста
        sbis_page.open()
        sbis_page.click_footer_download()
        sbis_dl.click_plugin_tab()
        sbis_dl.click_windows_tab()

        # Получаем ссылку на загрузку
        download_btn = sbis_dl.get_download_button()
        source = sbis_page.get_url_link(download_btn)

        # Проверяем корректность URL
        if not source.startswith("http"):
            raise ValueError(f"Некорректный URL: {source}")

        # Логируем информацию для отладки
        print(f"Скачиваем файл из: {source}")
        print(f"Сохраняем файл в: {file_path}")

        # Выполняем HTTP-запрос для скачивания файла
        response = requests.get(source)
        response.raise_for_status()  # Проверяем успешность запроса

        # Сохраняем файл
        sbis_dl.save_file(file_path, response.content)

        os.remove(file_path)
