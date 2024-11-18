from pages.SbisHomePage import SbisHomePage
from pages.SelectRegionMenu import RegionMenu

class TestCases:

    def test_case_02(self, driver):
        sbis_page = SbisHomePage(driver)
        region_menu = RegionMenu(driver)

        sbis_page.open()
        sbis_page.click_contacts()

        assert sbis_page.get_region_text() == "Свердловская обл."
        assert sbis_page.get_partners_text() != ""

        sbis_page.click_region()
        region_menu.select_region("Камчатский край")

        assert sbis_page.get_region_text() == "Камчатский край"
        assert "Петропавловск-Камчатский" in sbis_page.get_partners_text()
        assert driver.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
