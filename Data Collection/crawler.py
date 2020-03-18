'''
@Author: Shahzeb Afroze
Usecase: Crawler for the data from good reads

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import ActionChains
from pprint import pprint
import time

# makes sure that cookies are not saved - allows to scrape information without being noticed

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 

tags = ['Love', 'Life', 'Inspirational', 'Humor', 
        'Philosophy', 'God', 'Inspirational', 'Truth', 
        'Wisdom', 'Romance', 'Poetry', 'Death', 'Happiness', 
        'Hope', 'Faith', 'Writing', 'Inspiration', 'Quotes', 
        'Religion', 'Life', 'Success', 'Relationships', 
        'Motivational', 'Time', 'Knowledge', 'Love', 
        'Spirituality', 'Science', 'Books', 'Education']


number_of_tag = 0
with webdriver.Firefox(profile) as driver:
    for tag in tags:  
        # number of tags scraped
        number_of_tag+=1  
        driver.get(f"https://www.goodreads.com/quotes/tag/{tag}")

        # open datafile
        with open(f'scraped_data/{tag}.txt','a') as f:
            for page in range(99):
                # try:
                print(page)
            
                # scrape data

                # returns a list
                selection = driver.find_elements_by_class_name('quoteText')

                # length of selection
                length = len(selection)

                for i in range(length):
                    f.write(selection[i].text)
                    f.write('\n')
                    f.write('\n')

                time.sleep(3)
                # click to the next page
                next_page = driver.find_element_by_css_selector('a.next_page')
                
                # common error avoided
                next_page.location_once_scrolled_into_view

                # lets the page loaf properly
                driver.implicitly_wait(10)

                # leads to clicking signup on pop - needs further investigation
                # ActionChains(driver).move_to_element(next_page).click(next_page).perform()
                next_page.click()

                # debug
                # print(next_page)

                # only pop up in first page when the window opens so only the first tag
                if page == 0 and number_of_tag ==1:
                    time.sleep(3)
                    # click closing icon
                    # pop_up = driver.find_element_by_css_selector('button.gr-iconButton')
                    parentDiv = driver.find_elements_by_css_selector('div.modal__content')
                    child = parentDiv[1].find_element_by_css_selector('.modal__close')
                    pop_up = child.find_element_by_css_selector('.gr-iconButton')
                    # get into view SO: https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver/41744591
                    pop_up.location_once_scrolled_into_view
                    driver.implicitly_wait(10)
                    pop_up.click()

                # except:
                #     print(f"{page} last page for {tag}")
