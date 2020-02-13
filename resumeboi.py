from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os.path


driver = webdriver.Firefox(executable_path = r'C:\Users\janie\Documents\Projects\resumeBoi\geckodriver.exe')

driver.implicitly_wait(60000)

driver.maximize_window()

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

email_path = '//*[@id="username"]'
password_path = '//*[@id="password"]'
signin_path = '//*[@id="app__container"]/main/div/form/div[3]/button'
jobs_path = '//*[@id="jobs-nav-item"]/a'
jobList_path = '//*[@class="job-card-search__link-wrapper.js-focusable.disabled.ember-view"]'
nextjob_path = '//*[@class="job-card-search__link-wrapper.js-focusable.disabled.ember-view"]/following-sibling::p'

email_text = driver.find_element_by_xpath(email_path)
email_text.send_keys('arnold199926@gmail.com')

password_text = driver.find_element_by_xpath(password_path)
password_text.send_keys('Huy@123456')

signin_button = driver.find_element_by_xpath(signin_path)
signin_button.click()

jobs_button = driver.find_element_by_xpath(jobs_path)
jobs_button.click()

search_jobs_texts = driver.find_elements_by_class_name('jobs-search-box__text-input')
search_jobs_texts[0].send_keys('developer intern')


search_button = driver.find_element_by_class_name('jobs-search-box__submit-button.artdeco-button.artdeco-button--3.ml2')
search_button.click()

job_list = driver.find_elements_by_class_name("job-card-search__link-wrapper.js-focusable.disabled.ember-view")
# job_list = driver.find_elements_by_xpath(nextjob_path)

# deprecated
for job in job_list:
    job.click()
    driver.execute_script("arguments[0].scrollIntoView();", job )
    job_list.append(driver.find_element_by_class_name("job-card-search__link-wrapper.js-focusable.disabled.ember-view"))

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# page_bottom = driver.find_element_by_class_name("jobs-search-two-pane__pagination")

# ActionChains(driver).move_to_element(page_bottom).perform()