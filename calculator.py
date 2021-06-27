import time
import unittest

from selenium import webdriver

link="https://metaratings.ru/prognozy/futbol/stavki-i-koeffitsienty-na-pobeditelya-evro-2020/" #уточнить вечный URL
class CalculatorTesting(unittest.TestCase):
    value_summ_bet=10000
    value_kef=1.5


    def calc_win(self, bet,kef):
        return int(bet*kef-bet)

    def calc_payment(self, bet,kef):
        return int(bet*kef)

    def get_int_value(self, text):
        return int(text.replace(" ", ""))



    def test_calculator(self):
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            calculator_block=browser.find_element_by_class_name("rate-calculator.js-rate-calc.rate-calculator-initialized")

            summ_bet=browser.find_element_by_class_name("js-rate-calc-sum")
            summ_bet.send_keys(self.value_summ_bet)

            kef=browser.find_element_by_class_name("js-rate-calc-odd")
            kef.send_keys(str(self.value_kef))

            summ_win=browser.find_element_by_class_name("rate-calculator-winning-value.js-rate-calc-winning")
            etalon_win = self.calc_win(self.value_summ_bet, self.value_kef)


            pay=browser.find_element_by_class_name("rate-calculator-payment-value.js-rate-calc-payment")
            etalon_payment=self.calc_payment(self.value_summ_bet,self.value_kef)

            self.assertEqual(etalon_win,self.get_int_value(summ_win.text), "Сумма выигрыша некорректна")
            self.assertEqual(etalon_payment,self.get_int_value(pay.text), "Сумма выплаты некорректна")


        finally:
            browser.close()
