import pytest
from selenium import webdriver
from loguru import logger

# Настраиваем логирование
logger.add("logs/test_log.log", format="{time} {level} {message}", level="INFO", rotation="1 MB")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs['driver']
        driver.save_screenshot(f"logs/{item.name}.png")
        
@pytest.fixture(scope="function")
def driver():
    """Фикстура для работы с браузером."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logger.info("Закрытие веб-драйвера.")