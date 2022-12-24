from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException)


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': r'C:\Users\lucas\Downloads',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})


servico = Service(ChromeDriverManager().install())
drive = webdriver.Chrome(service=servico, options=options)
drive.maximize_window()
marktime = WebDriverWait(drive, 90)
