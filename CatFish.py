import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link="https://metaratings.ru/"

from  firstTests import *
class CatfishTesting(unittest.TestCase):

    def test_close_catfish(self):
        try:
             browser=webdriver.Chrome()
             browser.get(link)
             catfish_close=None
             element=None
             catfish_close=WebDriverWait(browser, 5).until(
                 EC.visibility_of_element_located((By.CLASS_NAME, "catfish-close"))
             )
             catfish_close.click()

             element = WebDriverWait(browser, 5).until(
                 EC.invisibility_of_element_located((By.CLASS_NAME, "catfish.comm-item"))
             )
        except TimeoutException:
            self.assertIsNotNone(catfish_close, "Не подгрузился catfish")
            self.assertIsNotNone(element, "Не закрылся catfish")

        finally:
            browser.close()


if __name__ == "__main__":
    unittest.main()