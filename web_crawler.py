from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def pull_ps_jobs():
    url = 'https://www.playstation.com/en-us/corporate/playstation-careers/#listings'
    driver = webdriver.Safari()
    wait = 3

    driver.get(url)
    driver.implicitly_wait(0.5)

    location_dropdown = driver.find_element(By.ID, "careers-locations")
    location_select = Select(location_dropdown)
    time.sleep(wait)

    location_select.select_by_visible_text('United States, Remote')
    time.sleep(wait)

    jobs = {x.text: x.get_attribute('href') for x in driver.find_elements(By.CLASS_NAME, "career-title")}
    print(jobs)
    return jobs

if __name__ == '__main__':
    pull_ps_jobs()
