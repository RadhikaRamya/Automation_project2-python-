import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    serv_obj = ChromeService(executable_path="F:\selenium webdrvrs\chromedriver.exe")
    return webdriver.Chrome(service=serv_obj)
