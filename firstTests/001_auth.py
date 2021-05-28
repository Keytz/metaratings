from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "https://metaratings.ru/"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    button_auth_open = browser.find_element_by_class_name("head-auth.js-modal-show")
    button_auth_open.click()
    form_auth=browser.find_element_by_class_name("auth-form.is-login.js-auth-action")

    input1_Email = form_auth.find_element_by_name("USER_EMAIL")
    input1_Email.send_keys("keytz@mail.ru")

    input2_password = form_auth.find_element_by_name("USER_PASSWORD")
    input2_password.send_keys("200393")

    button_submit=form_auth.find_element_by_class_name("auth-btn.js-auth-btn")
    button_submit.click()

    head_profile = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "head-profile.js-modal-show"))
    )
    head_profile.click()

    button_logout = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "head-profile-link"))
    )
    button_logout.click()

finally:
    time.sleep(30)

    browser.quit()
