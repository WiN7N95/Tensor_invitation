from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage

class TestCases:

    def test_case_01(self, driver):
        sbis_page = SbisHomePage(driver)
        tensor_page = TensorHomePage(driver)

        sbis_page.open()
        sbis_page.click_contacts()
        sbis_page.click_tensor_link()

        sbis_page.switch_windows(1)
        assert driver.current_url == "https://tensor.ru/"

        assert tensor_page.is_power_in_people_visible()

        tensor_page.click_more_link()
        assert driver.current_url == "https://tensor.ru/about"

        sizes = tensor_page.get_working_images_sizes()
        assert len(set(sizes)) == 1
