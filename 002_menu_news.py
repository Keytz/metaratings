import time

from selenium import webdriver

link="https://metaratings.ru/news/"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    icon_eksklyuzivy = browser.find_element_by_link_text("Эксклюзивы")
    icon_eksklyuzivy.click()

    icon_footbool = browser.find_element_by_link_text("Футбол")
    icon_footbool.click()

    icon_hokkey = browser.find_element_by_link_text("Хоккей")
    icon_hokkey.click()

    icon_tennis = browser.find_element_by_link_text("Теннис")
    icon_tennis.click()

    icon_basketbool = browser.find_element_by_link_text("Баскетбол")
    icon_basketbool.click()

    icon_voleytbool = browser.find_element_by_link_text("Волейбол")
    icon_voleytbool.click()

    icon_mma = browser.find_element_by_link_text("Единоборства")
    icon_mma.click()

    icon_other = browser.find_element_by_link_text("Другие")
    icon_other.click()

    icon_all = browser.find_element_by_link_text("Все")
    icon_all.click()


finally:
    time.sleep(3)
    browser.close()