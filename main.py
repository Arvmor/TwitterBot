#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import choice
from bs4 import BeautifulSoup
from sys import path

# you have to authorize your account with below api IF you want to unfollow people
# there is a high chance to get LIMIT while using below api


def unfollow2():
    unfurl = 'https://www.unfollowspy.com/twittersignin.php'
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(unfurl)
    sleep(20)
    unfurl = 'https://www.unfollowspy.com/notfollow.php'
    driver.get(unfurl)
    sleep(30)
    userf = 0
    totalunf = 0
    try:
        while totalunf != 100:
            while userf != 20:
                driver.find_element(
                    By.XPATH, '//*[@id="actionbutton'+str(userf)+'"]').location_once_scrolled_into_view
                driver.find_element(
                    By.XPATH, '//*[@id="actionbutton'+str(userf)+'"]').click()
                userf += 1
                totalunf += 1
                sleep(4)
            userf = 0
            driver.get(unfurl)
            sleep(15)
    except:
        pass

# you have to authorize your account with below api IF you want to unfollow people
# there is a high chance to get LIMIT while using below api


def unfollow():
    unfurl = 'https://iunfollow.com/accounts/twitter/login/?next=/nonfollow'
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(unfurl)
    sleep(30)
    userf = 100
    try:
        sleep(4)
        while userf != 51:
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(userf)+']/div[2]/button[1]').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(userf)+']/div[2]/button[1]').click()
            userf -= 1
            sleep(2)
    except:
        pass


def pintweet():
    try:
        # pin function with 1% chacne.
        pin = range(100)
        pin = choice(pin)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        if pin == 1:
            print("Pin : True")
            pinurl = "https://twitter.com/youraccountID"
            driver.get(pinurl)
            sleep(30)
            # basically pinning the last tweet
            flesh = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/div/div/article/div/div[2]/div[2]/div[1]/div/div/div[2]/div')))
            flesh.click()
            sleep(1)
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div[2]').click()
            sleep(1)
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]').click()
    except:
        pass
    sleep(2)


def retweet():
    # retweet function with many tweet sources which allows the bot to pick fresh tweets. with 1/15 chance.
    try:
        retwt = range(12)
        retwt = choice(retwt)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        if retwt == 1:
            print("Retweet: True")
            retwts = range(1)  # total retweet sources
            retwts = choice(retwts)
            retsource = ['user profile url for retweet source']
            rturl = retsource[retwts]
            driver.get(rturl)
            sleep(30)
            ret = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[2]/div')))
            ret.click()
            sleep(10)
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div').click()
    except:
        pass

# will close usless


def clear():
    sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def tweet():
    # tweet function, it will tweet whatever is in the twtext variable
    sturl = 'https://twitter.com/compose/tweet'
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(sturl)
    sleep(30)
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys("Hi, This is automated Twitter-BOT checkout https://github.com/Goodzilam/TwitterBot")
    sleep(2)
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
    sleep(2)


def follow_Proccess():
    # will randomly pick one of these below sources and then follow their n last followers
    simpland = ["someoneid"]
    simpn = range(1)  # number of total sources ***
    simpn = choice(simpn)
    fwurl = "https://twitter.com/"+simpland[simpn]+"/followers"
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(fwurl)
    sleep(30)
    # starts following
    acc = 1
    followed = 0
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
    while(followed != 18):
        try:
            sleep(1)
            acc += 1
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div['+str(acc-2)+']/div/div/div/div[2]/div[1]/div[2]/div').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
            followed += 1
        except:
            if driver.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]'):
                driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]').click()
                sleep(4)
    # going back to main menu


# driver settings
path.insert(0, '/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)
url = "https://twitter.com/login"
driver.get(url)
sleep(30)
# login
while True:
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys("username")
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys("password")
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
    sleep(2)
    try:
        if driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/span').text != "":
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys('email')
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys('password')
            sleep(2)
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
            sleep(2)
            break
    except:
        pass
    break
# the main code
runtimehour = 0
tweeted = False
# unfollow not followed-bck
try:
    unfollow2()
    clear()
    unfollow()
    clear()
except:
    pass
while True:
    # tbh i dont know how to handle crashes :3
    if runtimehour == 14:
        runtimehour = 0
        sleep(37000)
    while True:
        try:
            # selecets a random post and then it will tweet it
            if tweeted == False:
                pickpost()
                sleep(2)
                tweet()
                clear()
            tweeted = True
            sleep(2)
            # retweet with 1/15 chance
            retweet()
            clear()
            # pin the last tweet with 1% chance
            pintweet()
            clear()
            #  following Proccess
            follow_Proccess()
            clear()
            # checks for runtime hour
            runtimehour += 1
            tweeted = False
            print(f"All done ! {runtimehour}/14")
            if runtimehour == 14:
                break
            # here you can set the delay time
            sleep(3500)
        except Exception as excep:
            print("hitted an exception")
            print(excep)
            break
