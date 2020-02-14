import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import time

# specify browser of choice
driver = webdriver.Chrome(r'C:\Users\huytran\Projects\ResumeBoi\chromedriver.exe')

# prevent driver to stop running before finishing execution
driver.implicitly_wait(60000)

# specify linkedIn login page
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# specify Xpath for different web elements
email_path = '//*[@id="username"]'
password_path = '//*[@id="password"]'
signin_path = '//*[@id="app__container"]/main/div/form/div[3]/button'
jobs_path = '//*[@id="jobs-nav-item"]/a'
jobs_panel_path = '//*[@id="ember5"]/div[4]/div[3]/section[1]/div[2]/div/div/div[1]/div[2]'

# find email field and type in login email
email_text = driver.find_element_by_xpath(email_path)
email_text.send_keys('arnold199926@gmail.com')

# find password field and type in password
password_text = driver.find_element_by_xpath(password_path)
password_text.send_keys('Huy@123456')

# find signin button and click
signin_button = driver.find_element_by_xpath(signin_path)
signin_button.click()

# find jobs tab on newsfeed page and click
jobs_button = driver.find_element_by_xpath(jobs_path)
jobs_button.click()

# find search jobs box and insert search keywords
search_jobs_texts = driver.find_elements_by_class_name('jobs-search-box__text-input')
search_jobs_texts[0].send_keys('developer intern')

# find search button and click to execute the search
search_button = driver.find_element_by_class_name('jobs-search-box__submit-button.artdeco-button.artdeco-button--3.ml2')
search_button.click()

# find the panel that contain all the jobs and scroll to get all job elements
jobs_panel = driver.find_element_by_xpath(jobs_panel_path)
jobs_panel.send_keys(Keys.END)
time.sleep(2)
jobs_panel.send_keys(Keys.END)

# scroll down and click on every job on job list
'''
job_list = driver.find_elements_by_class_name("job-card-search__link-wrapper.js-focusable.disabled.ember-view")

count = 0
for job in job_list:
    job.click()
    count += 1

print(count)
'''

# get only easy apply jobs from the job panel
easy_apply_list = driver.find_elements_by_class_name('job-card-search__easy-apply')
for easy_apply in easy_apply_list:
    easy_apply.click()
