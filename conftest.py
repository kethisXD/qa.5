# tests/conftest.py
import pytest
from webDriverInit import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()