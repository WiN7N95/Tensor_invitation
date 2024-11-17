from pages.SbisHomePage import SbisHomePage
from pages.SelectRegionMenu import RegionMenu

class TestCases:

    def test_case_02(self, driver):
        """Тест-кейс №2"""

        kamchatskij_kraj_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        sver_obl = 'Свердловская обл.'
        kamchatskij_kraj = 'Камчатский край'
        petropavlovsk = 'Петропавловск-Камчатский'
        kamchatskij_kraj_title = 'СБИС Контакты — Камчатский край'

        sbis_page = SbisHomePage(driver)
        partners = RegionMenu(driver)

        # Шаг 1
        sbis_page.open()
        sbis_page.find_element(locator=sbis_page.contacts).click()

        # Шаг 2
        region_element = sbis_page.find_element(locator=sbis_page.region)
        sbis_page.check_region(region_name=sver_obl)
        sbis_page.check_displayed(element_locator=sbis_page.partners_list)
        print(f"Region before checking: '{region_element.text}'") # Показать результат в терминале
        
        # Шаг 3
        sbis_page.find_element(locator=sbis_page.region).click()
        partners.select_region(region_name=kamchatskij_kraj)

        # Шаг 4
        sbis_page.check_region(region_name=kamchatskij_kraj)
        sbis_page.check_partners_region(partner_text=petropavlovsk)
        sbis_page.check_current_url(url=kamchatskij_kraj_url)
        sbis_page.check_title(title=kamchatskij_kraj_title)
