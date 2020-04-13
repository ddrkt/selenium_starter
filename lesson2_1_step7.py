from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element_by_id("treasure")
    x = treasure_img.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[type='checkbox']")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
