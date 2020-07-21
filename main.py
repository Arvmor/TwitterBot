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
from sys import path, argv
from urllib.request import urlopen
from random import choice
import credentials


def unfollow2():
    # you have to authorize your account with below api IF you want to unfollow people
    # there is a high chance to get LIMIT while using below api
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.unfollowspy.com/twittersignin.php')
    sleep(20)
    driver.get('https://www.unfollowspy.com/notfollow.php')
    sleep(30)
    userPerPage = 0
    totalUnFollowed = 0
    try:
        while totalUnFollowed != 100:
            while userPerPage != 20:
                driver.find_element(
                    By.XPATH, '//*[@id="actionbutton'+str(userPerPage)+'"]').location_once_scrolled_into_view
                driver.find_element(
                    By.XPATH, '//*[@id="actionbutton'+str(userPerPage)+'"]').click()
                userPerPage += 1
                totalUnFollowed += 1
                sleep(4)
            userPerPage = 0
            driver.get('https://www.unfollowspy.com/notfollow.php')
            sleep(15)
    except:
        pass


def unfollow():
    # you have to authorize your account with below api IF you want to unfollow people
    # there is a high chance to get LIMIT while using below api
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://iunfollow.com/accounts/twitter/login/?next=/nonfollow')
    sleep(30)
    usersToUnFollow = 100
    try:
        sleep(4)
        while usersToUnFollow != 51:
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(usersToUnFollow)+']/div[2]/button[1]').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div[2]/ul/li['+str(usersToUnFollow)+']/div[2]/button[1]').click()
            usersToUnFollow -= 1
            sleep(2)
    except:
        pass


def pintweet():
    try:
        # pin function with 1% chance.
        pin = choice(range(100))
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        if pin == 1:
            print("Pin : True")
            driver.get(
                f"https://twitter.com/{credentials.account[int(argv[1])][0]}")
            sleep(30)
            # basically pinning the last tweet
            flesh = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div')))
            flesh.click()
            sleep(1)
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]').click()
            sleep(1)
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]').click()
    except:
        pass
    sleep(2)


def retweet():
    # retweet function with many tweet sources which allows the bot to pick fresh tweets. with 1/10 chance.
    try:
        retweetChance = choice(range(10))
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        if retweetChance == 1:
            print("Retweet: True")
            ProfileToSelectTweet = choice(
                range(len(credentials.retweetSource)))
            driver.get(
                f"https://twitter.com/{credentials.retweetSource[ProfileToSelectTweet]}")
            sleep(30)
            ret = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div')))
            ret.click()
            sleep(10)
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()
    except:
        pass


def clear():  # will close useless tabs
    sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def tweet(tweetText):
    # tweet function, it will tweet whatever is in the tweetText variable
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://twitter.com/compose/tweet')
    sleep(15)
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span').send_keys(tweetText)
    sleep(2)
    try:
        if driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]') and int(argv[1]) < 2:
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        else:
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]').click()
    except:
        pass
    sleep(2)


def pickpost():
    # it will pick a random post from telegram channel which in here is our tweet source
    postNumbers = choice(range(171509))
    page = urlopen(
        'https://t.me/OfficialPersianTwitter/'+str(postNumbers))
    soup = BeautifulSoup(page, "html.parser")
    url = soup.find("meta",  property="og:description")
    tweetText = url["content"].strip()
    ch = -24
    while abs(ch) != len(tweetText):
        if tweetText[ch] == '》' or tweetText[ch] == '×' or tweetText[ch] == '•' or tweetText[ch] == '»' or tweetText[ch] == '*' or tweetText[ch] == '※':
            tweetText = tweetText[:ch]
        ch -= 1
    tweetText = tweetText.strip()
    ch = -1
    while abs(ch) != len(tweetText):
        if tweetText[ch] == '×' or tweetText[ch] == '•' or tweetText[ch] == '*' or tweetText[ch] == '※':
            tweetText = tweetText[:ch]
        ch -= 1
    tweetText = tweetText.strip()
    if tweetText[1:5] == 'ادمی':
        if choice(range(5)) == 1:
            tweetText = credentials.errorText[choice(
                range(len(credentials.errorText)))]
            return tweetText
        else:
            tweetText = ''
    return tweetText


def follow_Proccess():
    # will randomly pick one of these below sources and then follow their n last followers
    randomNumber = choice(range(len(credentials.followIdList)))
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(
        f"https://twitter.com/{credentials.followIdList[randomNumber]}/followers")
    sleep(30)
    # starts following
    acc = 1
    followed = 0
    driver.find_element(
        By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
    while(followed != 25):
        try:
            sleep(1)
            acc += 1
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc-2)+']/div/div/div/div[2]/div[1]/div[2]/div').location_once_scrolled_into_view
            driver.find_element(
                By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['+str(acc)+']/div/div/div/div[2]/div[1]/div[2]/div').click()
            followed += 1
        except:
            if driver.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]'):
                driver.find_element(
                    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]').click()
                sleep(4)
    # going back to main menu


# driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--log-level=OFF")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://twitter.com/login")
sleep(15)
# login
while True:
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][0])
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][1])
    driver.find_element(
        By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
    sleep(2)
    try:
        if driver.find_element(By.XPATH, '/html/body/div[2]/div/p[3]/strong').text != '':
            driver.find_element(By.XPATH, '/html/body/div[2]/div/form/input[8]').send_keys(
                f"09{credentials.account[int(argv[1])][3]}")
            sleep(2)
            driver.find_element(
                By.XPATH, '/html/body/div[2]/div/form/input[9]').click()
            sleep(5)
            driver.get("https://twitter.com/login")
            break
        if driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/span').text != "":
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][2])
            driver.find_element(
                By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(credentials.account[int(argv[1])][1])
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
if argv[2] == 1:
    try:
        unfollow2()
        clear()
        unfollow()
        clear()
    except:
        pass
while True:
    if runtimehour == 14:
        runtimehour = 0
        sleep(37000)
    while True:
        try:
            # selects a random post and then tweet it
            if tweeted == False:
                sleep(2)
                tweet(pickpost())
                clear()
            tweeted = True
            sleep(2)
            # retweet with 1/10 chance
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
            print(f"All done ! {runtimehour}/28")
            if runtimehour == 14:
                break
            # here you can set the delay time
            sleep(choice(range(1700, 1800)))
        except Exception as excep:
            print("hitted an exception")
            print(excep)
            pass
