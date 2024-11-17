from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage

class TestCases:

    def test_case_01(self, driver):
        """Тест-кейс №1"""

        tensor_url = "https://tensor.ru/"
        tensor_about_url = 'https://tensor.ru/about'

        sbis_page = SbisHomePage(driver)
        tensor_page = TensorHomePage(driver)

        # Шаг 1
        sbis_page.open()
        sbis_page.find_element(locator=sbis_page.contacts).click()

        # Шаг 2
        sbis_page.find_element(locator=sbis_page.tensor_link).click()

        # Шаг 3
        sbis_page.switch_windows(window=1)
        sbis_page.check_current_url(url=tensor_url)

        # Шаг 4
        tensor_page.check_displayed(element_locator=TensorHomePage.power_in_people)

        # Шаг 5
        more_link = tensor_page.find_element(locator=TensorHomePage.more_link, arrow_down=True)
        more_link.click()
        sbis_page.check_current_url(url=tensor_about_url)

        # Шаг 6
        tensor_page.verify_working_images()

