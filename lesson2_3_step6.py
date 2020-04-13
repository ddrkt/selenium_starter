from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    trollface_button = browser.find_element_by_tag_name('button')
    trollface_button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    time.sleep(1)

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    input = browser.find_element_by_tag_name('input')
    input.send_keys(y)
    time.sleep(1)

    submit = browser.find_element_by_tag_name('button')
    submit.click()
    time.sleep(1)

finally:
    time.sleep(7)
    browser.quit()
