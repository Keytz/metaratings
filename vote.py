import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link="https://metaratings.ru/prognozy/futbol/ukraina-avstriya-prognoz-21-iyunya-2021/"

class VotTesting (unittest.TestCase):

    def test_vote (self):
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            checkbox=browser.find_element_by_id("vote-bet-0")
            browser.execute_script("arguments[0].click();", checkbox)

            button_vote=browser.find_element_by_class_name("vote-form-submit")
            browser.execute_script("arguments[0].click();", button_vote)

            element = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "vote-result"))
            )
        except:
            self.assertIsNot(element, "Голосование не прошло")

        finally:
            browser.close()
