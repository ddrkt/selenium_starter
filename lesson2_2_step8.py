from selenium import webdriver
import os
import time

REQUIRED_FIELDS = [
    {
        "locator": "[name='firstname']", "value": 'Anton'
    },
    {
        "locator": "[name='lastname']", "value": 'drkt'
    },
    {
        "locator": "[name='email']", "value": 'antonsh@dirokot.ru'
    }
]

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    for item in REQUIRED_FIELDS:
        browser.find_element_by_css_selector(item.get("locator")).send_keys(item.get("value"))

    current_dir = os.path.abspath(os.path.dirname(__file__))
    attachment = os.path.join(current_dir, 'test.txt')
    file_input = browser.find_element_by_css_selector("[type='file']")
    file_input.send_keys(attachment)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(7)
    browser.quit()
