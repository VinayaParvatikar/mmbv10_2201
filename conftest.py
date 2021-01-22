import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# @pytest.fixture(scope="class")
# def setup(request):
#     chromedriver_path = "C:\\Users\\vp094039\\Downloads\\chromedriver-v3.1.6-win32-ia32\\chromedriver"
#     electron_path = "C:\\Users\\vp094039\\AppData\\Local\\Programs\\mmb-ui\\Movie Magic Budgeting.exe"
#
#     opts = Options()
#     opts.binary_location = electron_path
#     driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)
#     request.cls.driver = driver
#     driver.implicitly_wait(15)
#     driver.find_element_by_id('username').send_keys('vinaya.parvatikar@accionlabs.com')
#     driver.find_element_by_id('password').send_keys('Welcome123$')
#     driver.find_element_by_id('signOnButton').click()
#     driver.implicitly_wait(15)
#     #driver.switch_to.window(driver.window_handles[0])
#     assert "Startup: Open Budgets" in driver.title
#
#     yield driver
#     winHandleBefore = driver.window_handles[0]
#     driver.switch_to.window(winHandleBefore)
#     driver.close()