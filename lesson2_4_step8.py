from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_button = browser.find_element_by_id('book')
    book_button.click()

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    input = browser.find_element_by_tag_name('input')
    input.send_keys(y)
    time.sleep(1)

    submit = browser.find_element_by_id('solve')
    submit.click()

finally:
    time.sleep(7)
    browser.quit()
